from rest_framework import viewsets
from .models import Token, Portfolio, PortfolioToken, UserProfile
from .serializers import TokenSerializer, PortfolioSerializer, PortfolioTokenSerializer, UserProfileSerializer
from cpm.api_intergration.coin_gecko_api import CoinGeckoAPI  # Importing the API integration
from rest_framework.response import Response

class TokenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

    def list(self, request, *args, **kwargs):
        # Fetch tokens from the database or other source
        queryset = self.get_queryset()  # Fetch tokens queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioTokenViewSet(viewsets.ModelViewSet):
    queryset = PortfolioToken.objects.all()
    serializer_class = PortfolioTokenSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

def save_tokens_to_db():
    token_data = CoinGeckoAPI.get_tokens()
    
    for token_info in token_data:
        token, created = Token.objects.get_or_create(
            name=token_info['name'],
            symbol=token_info['symbol'],
            current_price=token_info['current_price']
            # Add other fields as needed
        )

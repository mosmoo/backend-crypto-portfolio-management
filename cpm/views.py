from rest_framework import viewsets
from .models import Token, Portfolio, PortfolioToken, UserProfile
from .serializers import TokenSerializer, PortfolioSerializer, PortfolioTokenSerializer, UserProfileSerializer
from cpm.api_intergration.coin_gecko_api import CoinGeckoAPI  # Importing the API integration
from rest_framework.response import Response
from rest_framework import status

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

    # Custom action to fetch and return market data for a specific token
    def fetch_market_data(self, request, pk=None):
        token = self.get_object()
        market_data = CoinGeckoAPI.get_token_market_data(token.token_id)  # Assuming token_id field in the Token model
        # Process or store the market data as needed
        return Response(market_data, status=status.HTTP_200_OK)
        # Return or further process the fetched data
    
class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioTokenViewSet(viewsets.ModelViewSet):
    queryset = PortfolioToken.objects.all()
    serializer_class = PortfolioTokenSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Create your views here.

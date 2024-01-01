from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TokenViewSet, PortfolioViewSet, PortfolioTokenViewSet, UserProfileViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'tokens', TokenViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'portfolio-tokens', PortfolioTokenViewSet)
router.register(r'user-profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Define other URLs if needed
]

# Optionally, if you want to include custom actions
urlpatterns += [
    path('tokens/<int:pk>/fetch-market-data/', TokenViewSet.as_view({'get': 'fetch_market_data'}), name='token-fetch-market-data'),
    # Define other custom endpoints if required
]

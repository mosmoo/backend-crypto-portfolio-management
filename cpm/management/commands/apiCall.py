from django.core.management.base import BaseCommand
from cpm.models import Token
from cpm.api_intergration.coin_gecko_api import CoinGeckoAPI

class Command(BaseCommand):
    help = 'Your helpful description for this command'

    def handle(self, *args, **kwargs):
        # Fetch tokens from CoinGeckoAPI
        token_data = CoinGeckoAPI.get_tokens()

        # Save tokens to your Token model
        for token_info in token_data:
            try:
                # Access token details from the response and handle missing keys
                name = token_info.get('name', 'Unknown')
                symbol = token_info.get('symbol', 'Unknown')
                # Fetch current price or handle if the key is missing
                current_price = token_info.get('current_price', 0.0)  # Default value if key is missing

                # Save or update token in the database
                Token.objects.update_or_create(
                    name=name,
                    symbol=symbol,
                    defaults={'current_price': current_price}
                    # Add other fields as needed
                )
            except Exception as e:
                # Handle exceptions or log errors
                print(f"Error processing token: {e}")
        
        self.stdout.write(self.style.SUCCESS('Tokens added/updated successfully'))

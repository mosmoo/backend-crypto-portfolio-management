import requests

class CoinGeckoAPI:
    BASE_URL = 'https://api.coingecko.com/api/v3'

    @classmethod
    def get_tokens(cls):
        url = f'{cls.BASE_URL}/coins/markets?vs_currency=usd'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()  # Process and return token data
            else:
                # Handle other status codes or errors here
                return None
        except requests.RequestException as e:
            # Log or handle connection errors
            print(f"Request Exception: {e}")
            return None

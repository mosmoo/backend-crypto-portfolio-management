import requests

class CoinGeckoAPI:
    BASE_URL = 'https://api.coingecko.com/api/v3'

    @classmethod
    def get_token_market_data(cls, token_id):
        url = f'{cls.BASE_URL}/coins/markets?vs_currency=usd&ids={token_id}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()  # Process this data as needed
            else:
                # Handle other status codes or errors here
                return None
        except requests.RequestException as e:
            # Log or handle connection errors
            print(f"Request Exception: {e}")
            return None

import requests
import json
import time
from functools import wraps

# Decorator to cache exchange rates to avoid repeated API calls
def cache_rates(func):
    cache = {}
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not cache:
            cache['rates'] = func(self, *args, **kwargs)
            cache['timestamp'] = time.time()
        elif time.time() - cache['timestamp'] > 3600:  # Cache expires after 1 hour
            cache['rates'] = func(self, *args, **kwargs)
            cache['timestamp'] = time.time()
        return cache['rates']
    return wrapper

# CurrencyConverter class
class CurrencyConverter:
    def __init__(self, api_key, base_currency='USD'):
        self.api_key = api_key
        self.base_currency = base_currency
        self.api_url = 'https://api.currencyapi.com/v3/latest'

    @cache_rates
    def fetch_exchange_rates(self):
        url = f'{self.api_url}?apikey={self.api_key}&base_currency={self.base_currency}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['meta']['success']:
                return data['data']
            else:
                raise ValueError(f"API Error: {data['meta']['error_message']}")
        else:
            raise ConnectionError(f"Failed to fetch data: {response.status_code}")

    def convert(self, amount, from_currency, to_currency):
        rates = self.fetch_exchange_rates()
        if from_currency == self.base_currency:
            base_amount = amount
        else:
            base_amount = amount / rates[from_currency]['value']
        if to_currency == self.base_currency:
            return base_amount
        else:
            return base_amount * rates[to_currency]['value']

    def list_supported_currencies(self):
        rates = self.fetch_exchange_rates()
        return list(rates.keys())

    def historical_rates(self, from_currency, to_currency, days=30):
        # Mock data for historical rates
        for day in range(days):
            yield {
                'date': f'2025-08-{day+1:02}',
                'rate': round(self.convert(1, from_currency, to_currency), 2)
            }

# Example usage
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    converter = CurrencyConverter(api_key)

    # Convert 100 USD to EUR
    amount_in_eur = converter.convert(100, 'USD', 'EUR')
    print(f"100 USD = {amount_in_eur} EUR")

    # List supported currencies
    supported_currencies = converter.list_supported_currencies()
    print("Supported Currencies:", supported_currencies)

    # Display historical rates for USD to EUR
    print("\nHistorical Rates (last 30 days):")
    for rate in converter.historical_rates('USD', 'EUR'):
        print(rate)

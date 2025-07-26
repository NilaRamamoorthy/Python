import requests
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

FAV_FILE = 'favorites.txt'

def get_latest_rates(base='USD'):
    url = f"https://api.exchangerate.host/latest?base={base}"
    res = requests.get(url)
    data = res.json()
    return data['rates']

def convert_currency(amount, from_currency, to_currency):
    rates = get_latest_rates(from_currency)
    if to_currency not in rates:
        print(f"Currency {to_currency} not found.")
        return None
    converted = amount * rates[to_currency]
    return converted

def get_historical_rates(base, symbol, days=7):
    end = datetime.now()
    start = end - timedelta(days=days)
    url = (f"https://api.exchangerate.host/timeseries?"
           f"start_date={start.strftime('%Y-%m-%d')}&"
           f"end_date={end.strftime('%Y-%m-%d')}&"
           f"base={base}&symbols={symbol}")
    res = requests.get(url)
    data = res.json()
    if not data['success']:
        print("Failed to fetch historical data.")
        return None
    rates = data['rates']
    dates = sorted(rates.keys())
    values = [rates[date][symbol] for date in dates]
    return dates, values

def plot_trend(dates, values, base, symbol):
    plt.plot(dates, values, marker='o')
    plt.title(f'{base} to {symbol} exchange rate trend')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def save_favorite(currency):
    try:
        with open(FAV_FILE, 'a') as f:
            f.write(currency.upper() + '\n')
        print(f"{currency} added to favorites.")
    except Exception as e:
        print("Error saving favorite:", e)

def load_favorites():
    if not os.path.exists(FAV_FILE):
        return []
    with open(FAV_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

def main():
    import os
    print("Currency Converter")
    favorites = load_favorites()
    while True:
        print("\nMenu:")
        print("1. Convert Currency")
        print("2. View Favorite Currencies")
        print("3. Historical Rate Lookup & Trend")
        print("4. Add Favorite Currency")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            amount = float(input("Amount: "))
            from_cur = input("From currency (e.g. USD): ").upper()
            to_cur = input("To currency (e.g. EUR): ").upper()
            result = convert_currency(amount, from_cur, to_cur)
            if result is not None:
                print(f"{amount} {from_cur} = {result:.4f} {to_cur}")

        elif choice == '2':
            if favorites:
                print("Favorite currencies:", ', '.join(favorites))
            else:
                print("No favorite currencies saved.")

        elif choice == '3':
            base = input("Base currency: ").upper()
            symbol = input("Target currency: ").upper()
            days = int(input("Days for historical data (e.g. 7): "))
            data = get_historical_rates(base, symbol, days)
            if data:
                dates, values = data
                print(f"Rates for last {days} days:")
                for d, v in zip(dates, values):
                    print(f"{d}: {v}")
                plot_trend(dates, values, base, symbol)

        elif choice == '4':
            cur = input("Currency to add to favorites: ").upper()
            save_favorite(cur)
            favorites = load_favorites()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

import requests
import json
import os

API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your OpenWeatherMap API key
FAV_FILE = 'favorites.json'

class WeatherApp:
    def __init__(self):
        self.favorites = self.load_favorites()
        self.units = 'metric'  # metric = Celsius, imperial = Fahrenheit

    def load_favorites(self):
        if os.path.exists(FAV_FILE):
            with open(FAV_FILE, 'r') as f:
                return json.load(f)
        return []

    def save_favorites(self):
        with open(FAV_FILE, 'w') as f:
            json.dump(self.favorites, f)

    def get_weather(self, location):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units={self.units}"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            self.display_current_weather(data)
        else:
            print("Location not found or API error.")

    def get_forecast(self, location):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units={self.units}"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            self.display_forecast(data)
        else:
            print("Location not found or API error.")

    def display_current_weather(self, data):
        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}° {'C' if self.units == 'metric' else 'F'}")
        print(f"Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind speed: {data['wind']['speed']} m/s")

    def display_forecast(self, data):
        print("\n5-day Forecast (3-hour intervals):")
        for item in data['list'][:40]:  # 5 days * 8 intervals/day
            time = item['dt_txt']
            temp = item['main']['temp']
            desc = item['weather'][0]['description']
            print(f"{time}: {temp}°, {desc}")

    def toggle_units(self):
        if self.units == 'metric':
            self.units = 'imperial'
            print("Units set to Fahrenheit.")
        else:
            self.units = 'metric'
            print("Units set to Celsius.")

    def add_favorite(self, location):
        if location not in self.favorites:
            self.favorites.append(location)
            self.save_favorites()
            print(f"{location} added to favorites.")
        else:
            print("Location already in favorites.")

    def list_favorites(self):
        if not self.favorites:
            print("No favorite locations saved.")
            return
        print("Favorite Locations:")
        for loc in self.favorites:
            print(f"- {loc}")

def main():
    app = WeatherApp()

    while True:
        print("\nMenu:")
        print("1. Get current weather")
        print("2. Get 5-day forecast")
        print("3. Toggle temperature units (C/F)")
        print("4. Add favorite location")
        print("5. List favorite locations")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            loc = input("Enter location (city name): ")
            app.get_weather(loc)

        elif choice == '2':
            loc = input("Enter location (city name): ")
            app.get_forecast(loc)

        elif choice == '3':
            app.toggle_units()

        elif choice == '4':
            loc = input("Enter location to add to favorites: ")
            app.add_favorite(loc)

        elif choice == '5':
            app.list_favorites()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

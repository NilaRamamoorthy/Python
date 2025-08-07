
import requests
import time
import json

# ========== Decorator ==========
def retry(func):
    def wrapper(*args, **kwargs):
        retries = 3
        for attempt in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[!] Attempt {attempt + 1} failed: {e}")
                time.sleep(1)
        print("[✖] Failed after 3 attempts.")
        return None
    return wrapper

# ========== OOP ==========
class Weather:
    def __init__(self, city, data):
        self.city = city
        self.temp = data['main']['temp']
        self.humidity = data['main']['humidity']
        self.description = data['weather'][0]['description']
        self.wind_speed = data['wind']['speed']

    def display(self):
        print(f"\n[🌦️] Weather in {self.city.upper()}:")
        print(f"   Temperature: {self.temp}°C")
        print(f"   Humidity: {self.humidity}%")
        print(f"   Description: {self.description.title()}")
        print(f"   Wind Speed: {self.wind_speed} m/s")

    def to_dict(self):
        return {
            "city": self.city,
            "temperature": self.temp,
            "humidity": self.humidity,
            "description": self.description,
            "wind_speed": self.wind_speed
        }

# ========== API Logic ==========
class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.history_file = "weather_history.json"

    @retry
    def get_weather_data(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code} - {response.text}")
        return response.json()

    def save_to_log(self, weather_obj):
        try:
            with open(self.history_file, "a") as f:
                f.write(json.dumps(weather_obj.to_dict()) + "\n")
        except Exception as e:
            print(f"[!] Could not save log: {e}")

    def run(self):
        print("🌍 Weather App\n")
        while True:
            city = input("Enter city (or 'exit' to quit): ").strip()
            if city.lower() == 'exit':
                break
            data = self.get_weather_data(city)
            if data:
                weather = Weather(city, data)
                weather.display()
                self.save_to_log(weather)

# ========== Generator: Forecast ==========
def forecast_generator(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "cnt": 24  # 3 days x 8 intervals (3-hour each)
    }
    try:
        response = requests.get(url, params=params)
        forecast_data = response.json()
        if response.status_code != 200:
            raise Exception(f"Forecast API Error: {forecast_data}")
        for i in range(0, len(forecast_data['list']), 8):  # Every 24 hours
            entry = forecast_data['list'][i]
            yield {
                "date": entry['dt_txt'],
                "temp": entry['main']['temp'],
                "desc": entry['weather'][0]['description']
            }
    except Exception as e:
        print(f"[!] Forecast Error: {e}")
        yield from ()

# ========== Main ==========
if __name__ == "__main__":
    API_KEY = "your_openweathermap_api_key_here"  # 🔑 Replace with your key
    app = WeatherApp(API_KEY)
    app.run()

    # Forecast Example
    city = input("\nWant a 3-day forecast? Enter city name: ")
    for day in forecast_generator(city, API_KEY):
        print(f"{day['date']} - {day['temp']}°C - {day['desc'].title()}")

import weather.api as weather_api
import weather.formatter as weather_formatter

def run_weather_app():
    city = input("Enter city name: ")
    data = weather_api.fetch_weather(city)
    output = weather_formatter.format_weather(data)
    print(output)

if __name__ == "__main__":
    run_weather_app()

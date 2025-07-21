# main.py

from weather_data import add_weather, get_weather
from report import display_weather_report, monthly_summary

# Add sample data
add_weather("2025-07-18", 33, 60, "sunny")
add_weather("2025-07-19", 30, 70, "cloudy")
add_weather("2025-07-20", 28, 85, "rainy")

# View specific day's weather
print("\nWeather on 2025-07-18:")
print(get_weather("2025-07-18"))

# Display full report
display_weather_report()

# Monthly summary
monthly_summary()

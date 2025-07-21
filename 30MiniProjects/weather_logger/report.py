# report.py

from typing import Dict, Tuple
from weather_data import get_all_data

def display_weather_report():
    print("\nWeather Report:")
    for date, (temp, humidity, condition) in get_all_data().items():
        print(f"{date}: Temp={temp}°C, Humidity={humidity}%, Condition={condition.title()}")

def monthly_summary():
    temps = []
    humidities = []
    conditions = set()

    for temp, humidity, condition in get_all_data().values():
        temps.append(temp)
        humidities.append(humidity)
        conditions.add(condition)

    if temps:
        avg_temp = sum(temps) / len(temps)
        avg_humidity = sum(humidities) / len(humidities)
        print(f"\nMonthly Summary:")
        print(f"Average Temperature: {avg_temp:.1f}°C")
        print(f"Average Humidity: {avg_humidity:.1f}%")
        print(f"Unique Weather Conditions: {', '.join(conditions)}")
    else:
        print("No data available for summary.")

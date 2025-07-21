# weather_data.py

from typing import Dict, Tuple

# Data format: date (YYYY-MM-DD) → (temperature, humidity, condition)
weather_log: Dict[str, Tuple[int, int, str]] = {}

def add_weather(date: str, temperature: int, humidity: int, condition: str):
    weather_log[date] = (temperature, humidity, condition.lower())
    print(f"Weather data added for {date}.")

def get_weather(date: str) -> Tuple[int, int, str]:
    return weather_log.get(date, ("No data", "No data", "No data"))

def get_all_data() -> Dict[str, Tuple[int, int, str]]:
    return weather_log

import json
from datetime import datetime

# Mock function to simulate weather API call
def fetch_weather(city):
    mock_data = {
        "city": city,
        "temperature": 28,
        "condition": "Sunny",
        "humidity": 50,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return mock_data

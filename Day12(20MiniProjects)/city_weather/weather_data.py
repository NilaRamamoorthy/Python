# weather_data.py

# Sample city weather data using (latitude, longitude) as key
weather_info = {
    (28.6139, 77.2090): {"city": "Delhi", "temp": 34, "condition": "Sunny"},
    (19.0760, 72.8777): {"city": "Mumbai", "temp": 30, "condition": "Humid"},
    (13.0827, 80.2707): {"city": "Chennai", "temp": 33, "condition": "Cloudy"},
    (22.5726, 88.3639): {"city": "Kolkata", "temp": 31, "condition": "Rainy"}
}

def get_weather_by_coords(lat, lon):
    key = (lat, lon)
    if key in weather_info:
        return weather_info[key]
    else:
        return None

def print_weather_report(info):
    if info:
        print(f"Weather Report for {info['city']}:")
        print(f"Temperature: {info['temp']}°C")
        print(f"Condition: {info['condition']}\n")
    else:
        print("Weather data not available for these coordinates.\n")

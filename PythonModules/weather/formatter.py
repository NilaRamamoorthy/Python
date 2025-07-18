def format_weather(data):
    return (
        f"\nWeather Report for {data['city']}:\n"
        f"Date: {data['date']}\n"
        f"Temperature: {data['temperature']}°C\n"
        f"Condition: {data['condition']}\n"
        f"Humidity: {data['humidity']}%\n"
    )

# main.py

from weather_data import get_weather_by_coords, print_weather_report

# Set to track visited cities
visited = set()

# Test coordinates to query
coordinates_list = [
    (28.6139, 77.2090),  # Delhi
    (19.0760, 72.8777),  # Mumbai
    (13.0827, 80.2707),  # Chennai
    (28.6139, 77.2090)   # Delhi again
]

for lat, lon in coordinates_list:
    city_info = get_weather_by_coords(lat, lon)
    if city_info:
        city_name = city_info["city"]
        if city_name in visited:
            print(f"Already visited {city_name}. Skipping duplicate...\n")
        else:
            visited.add(city_name)
            print_weather_report(city_info)
    else:
        print_weather_report(None)

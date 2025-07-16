# Initial temperature data
weather = {
    "Chennai": [34, 36, 35],
    "Delhi": [38, 37, 39],
    "Mumbai": [32, 31, 30]
}

# 1. Add new temperature reading
weather["Chennai"].append(33)
weather["Delhi"].append(40)

# 2. Calculate average temperature
city_avg_temp = {}
for city, temps in weather.items():
    avg = sum(temps) / len(temps)
    city_avg_temp[city] = round(avg, 2)

# 3. Sort cities by hottest average
sorted_cities = sorted(city_avg_temp.items(), key=lambda x: x[1], reverse=True)

print("Average Temperature by City (Hottest to Coolest):")
for city, avg in sorted_cities:
    print(f"{city}: {avg}°C")

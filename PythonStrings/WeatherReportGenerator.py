#12. Weather Report Generator

city=input("Enter city: ").strip()
temperature=input("Enter temperature(°C): ")
humidity=input("Enter Humidity: ").strip()
# f-string
print(f"Weather in {city}: {temperature}°C, {humidity}% humidity")
# concatination
print("Weather in "+city+": "+temperature+"°C, "+humidity+"% humidity")
# .formate()
print("Weather in {}: {}°C, {}% humidity".format(city,temperature,humidity))
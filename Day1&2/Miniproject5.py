celsius = input("Enter temperature in Celsius: ")
print(f"Before conversion: {celsius} (Type: {type(celsius)})")
celsius = float(celsius)
fahrenheit = (celsius * 9/5) + 32
print(f"\n{celsius}°C is equal to {fahrenheit}°F")
print(f"After conversion: {celsius} (Type: {type(celsius)})")

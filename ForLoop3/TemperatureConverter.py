#  5. Temperature Converter & Category
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
if celsius < 20:
    condition = "Cold"
elif celsius <= 30:
    condition = "Warm"
else:
    condition = "Hot"
print(f"{celsius}°C is {fahrenheit}°F - {condition}")
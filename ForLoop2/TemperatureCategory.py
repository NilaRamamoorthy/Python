temps = [float(input("Enter temperature: ")) for _ in range(5)]
for t in temps:
    if t < 20:
        print(f"{t}°C - Cold")
    elif t <= 30:
        print(f"{t}°C - Warm")
    else:
        print(f"{t}°C - Hot")
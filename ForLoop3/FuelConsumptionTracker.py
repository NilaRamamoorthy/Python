# 17. Fuel Consumption Tracker
fuel = [float(input(f"Day {i+1} fuel (litres): ")) for i in range(7)]
total = sum(fuel)
print(f"Total fuel used: {total} litres")
if total > 50:
    print("Fuel usage alert!")
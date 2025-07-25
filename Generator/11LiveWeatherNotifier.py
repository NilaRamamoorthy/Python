import random

def weather_notifier(initial=25):
    prev = initial
    while True:
        new_temp = random.randint(prev - 3, prev + 3)
        yield new_temp, abs(new_temp - prev)
        prev = new_temp

# Wrap with filtering generator expression
gen = (temp for temp, diff in weather_notifier(25) if diff >= 5)

print("Temperature changes ≥ ±5°C:")
count = 0
for temp in gen:
    print(temp, end=" ")
    count += 1
    if count >= 10:  # stop after 10 significant changes
        break
print("\nNotifier stopped after 10 alerts.")

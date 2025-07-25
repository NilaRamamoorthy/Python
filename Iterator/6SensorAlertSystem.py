import random

# Callable function generating sensor values
def read_sensor():
    return random.randint(0, 100)

# Create an iterator that keeps calling read_sensor until it returns exactly 99
sensor_iter = iter(read_sensor, 99)

print("Sensor readings until critical threshold (99):")
count = 0
for val in sensor_iter:
    print(val, end=" ")
    count += 1
print(f"\nALERT! Sensor reached critical value 99 after {count} readings.")
# When read_sensor() returns 99, iter() causes StopIteration and loop ends.

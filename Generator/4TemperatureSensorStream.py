import random
import time

def sensor_read():
    """Simulates a random sensor read from 0 to 110."""
    return random.randint(80, 110)

# Iterator stops when callable returns a value >100 (treated as sentinel)
sensor_iter = iter(sensor_read, 101)

print("Sensor readings (until >100):")
count = 0
for val in sensor_iter:
    # We only get values <101
    print(val, end=" ")
    count += 1
    if count >= 10:  # safety break to avoid too long runs
        break
print("\nStream stopped when temperature >100 reached (or count limit)")

# option2

def sensor_generator():
    while True:
        override = yield sensor_read()
        if override is not None:
            yield override

gen = sensor_generator()
reading = next(gen)  # initialize
print("Reading:", reading)
print("Inject override:", gen.send(105))  # override reading output
# gen.close()

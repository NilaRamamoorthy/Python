import functools
import random

def alert_on_threshold(threshold):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f"[ALERT] {func.__name__} returned {result}, which exceeds the threshold of {threshold}!")
            else:
                print(f"[INFO] {func.__name__} returned {result}.")
            return result
        return wrapper
    return decorator

# Example: Simulate temperature sensor reading
@alert_on_threshold(threshold=75)
def read_temperature():
    return random.randint(60, 90)

# Run simulation
for _ in range(5):
    read_temperature()

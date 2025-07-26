import functools
import time

def retry(max_retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_retries:
                try:
                    print(f"Attempt {attempt + 1} for '{func.__name__}'")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    attempt += 1
            print(f"Function '{func.__name__}' failed after {max_retries} attempts.")
        return wrapper
    return decorator

# Example usage
import random

@retry(max_retries=3, delay=2)
def unstable_network_call():
    if random.choice([True, False]):
        print("Network call succeeded.")
    else:
        raise ConnectionError("Simulated network failure.")

# Sample call
unstable_network_call()

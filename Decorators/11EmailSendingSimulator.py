import functools
import time
import random

# Retry decorator
def retry(max_retries=2, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts <= max_retries:
                try:
                    result = func(*args, **kwargs)
                    print(f"Attempt {attempts + 1}: Success")
                    return result
                except Exception as e:
                    print(f"Attempt {attempts + 1}: Failed with error: {e}")
                    attempts += 1
                    if attempts > max_retries:
                        print(f"Function '{func.__name__}' failed after {max_retries} retries.")
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

# Logging decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Result: {result}")
        return result
    return wrapper

# Simulated email sender function
@retry(max_retries=2, delay=1)
@log
def send_email(to, subject, message):
    if random.choice([True, False]):
        raise ConnectionError("Simulated email failure.")
    return f"Email sent to {to} with subject '{subject}'"

# Example usage
send_email("test@example.com", "Welcome!", "Hello and welcome to our platform.")

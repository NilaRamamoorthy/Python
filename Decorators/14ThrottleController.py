import time
import functools
from collections import deque

def throttle(limit):
    def decorator(func):
        call_times = deque()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()

            # Remove timestamps older than 60 seconds
            while call_times and current_time - call_times[0] > 60:
                call_times.popleft()

            if len(call_times) >= limit:
                print(f"[Throttle] Call blocked for {func.__name__} at {time.ctime(current_time)}")
                raise Exception(f"Rate limit exceeded: only {limit} calls per minute allowed.")

            call_times.append(current_time)
            return func(*args, **kwargs)

        return wrapper
    return decorator

# Example usage
@throttle(3)
def test_api():
    print("Function executed.")

# Simulate function calls
for i in range(5):
    try:
        test_api()
    except Exception as e:
        print(e)
    time.sleep(10)  # Adjust for testing (call more frequently to trigger block)

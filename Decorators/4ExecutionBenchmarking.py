import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"[{func.__name__}] executed in {duration:.4f} seconds")
        return result
    return wrapper

# Example usage
@timeit
def slow_operation():
    time.sleep(1.5)
    print("Slow operation completed.")

@timeit
def fast_operation():
    print("Fast operation completed.")

# Sample calls
slow_operation()
fast_operation()

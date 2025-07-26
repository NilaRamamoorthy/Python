import functools

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Fetching from cache for {func.__name__}{args}")
            return cache[args]
        print(f"Computing and caching result for {func.__name__}{args}")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

# Example usage
@memoize
def slow_add(a, b):
    import time
    time.sleep(1)  # Simulate delay
    return a + b

print(slow_add(5, 3))   # Computes
print(slow_add(5, 3))   # Cached
print(slow_add(4, 2))   # Computes
print(slow_add(4, 2))   # Cached

import time
import functools

# Decorator: Validate that inputs are numeric
def validate_numeric_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("All arguments must be numeric.")
        return func(*args, **kwargs)
    return wrapper

# Decorator: Log the output of the function
def log_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

# Decorator: Time how long a function takes
def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

# Math functions with all three decorators
@timeit
@log_output
@validate_numeric_input
def add(a, b):
    return a + b

@timeit
@log_output
@validate_numeric_input
def multiply(a, b):
    return a * b

@timeit
@log_output
@validate_numeric_input
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Example usage
add(10, 5)
multiply(3, 4)
try:
    divide(10, 0)
except ValueError as e:
    print(e)

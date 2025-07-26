import functools

def validate_types(*expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected):
                    raise TypeError(f"Argument {i+1} must be {expected.__name__}, got {type(arg).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example functions
@validate_types(int, int)
def add(a, b):
    return a + b

@validate_types(str, str)
def concat(a, b):
    return a + b

# Sample calls
print(add(10, 20))       # Valid
print(concat("Hi", "ya"))  # Valid

# Uncomment below lines to test errors
# print(add(10, "20"))     # Raises TypeError
# print(concat("Hi", 5))   # Raises TypeError

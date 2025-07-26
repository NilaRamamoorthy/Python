import functools

def log_methods(cls):
    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)
        if callable(attr) and not attr_name.startswith("__"):
            @functools.wraps(attr)
            def wrapper(self, *args, __func=attr, **kwargs):
                print(f"[LOG] Calling {__func.__name__} with args: {args}, kwargs: {kwargs}")
                return __func(self, *args, **kwargs)
            setattr(cls, attr_name, wrapper)
    return cls

@log_methods
class Calculator:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y if y != 0 else "Error: Division by zero"

# Example usage
calc = Calculator()
print(calc.add(3, 5))
print(calc.multiply(4, 6))
print(calc.divide(10, 2))

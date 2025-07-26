import functools

# Decorator to remove nulls from a list
def remove_nulls(func):
    @functools.wraps(func)
    def wrapper(data):
        cleaned = [item for item in data if item is not None]
        return func(cleaned)
    return wrapper

# Decorator to strip whitespace
def strip_whitespace(func):
    @functools.wraps(func)
    def wrapper(data):
        cleaned = [item.strip() if isinstance(item, str) else item for item in data]
        return func(cleaned)
    return wrapper

# Decorator to convert to lowercase
def lowercase_strings(func):
    @functools.wraps(func)
    def wrapper(data):
        cleaned = [item.lower() if isinstance(item, str) else item for item in data]
        return func(cleaned)
    return wrapper

# Chain all three decorators
@remove_nulls
@strip_whitespace
@lowercase_strings
def clean_data(data):
    return data

# Example usage
raw_data = ["  Apple ", None, " BANANA", "  mango  ", None, "OrAnGe  "]
cleaned = clean_data(raw_data)
print("Cleaned Data:", cleaned)

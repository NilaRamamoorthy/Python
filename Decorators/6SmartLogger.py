import functools
import datetime

def smart_logger(log_level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_message = f"[{log_level}] {timestamp} - Function: {func.__name__}, Result: {result}\n"
                return result
            except Exception as e:
                log_message = f"[ERROR] {timestamp} - Function: {func.__name__}, Error: {str(e)}\n"
                raise
            finally:
                with open("log.txt", "a") as log_file:
                    log_file.write(log_message)
        return wrapper
    return decorator

# Example usage
@smart_logger(log_level="DEBUG")
def multiply(a, b):
    return a * b

@smart_logger(log_level="INFO")
def divide(a, b):
    return a / b

# Sample calls
multiply(3, 4)
try:
    divide(10, 0)
except ZeroDivisionError:
    pass

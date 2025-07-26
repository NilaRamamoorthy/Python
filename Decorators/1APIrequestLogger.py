import functools
import datetime

# Decorator to log API request
def api_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log_entry = {
            "function": func.__name__,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "args": args,
            "kwargs": kwargs
        }
        try:
            result = func(*args, **kwargs)
            log_entry["status"] = "Success"
        except Exception as e:
            log_entry["status"] = f"Fail ({str(e)})"
            result = None
        print(log_entry)
        return result
    return wrapper

# Example usage
@api_logger
def get_user_data(user_id):
    if user_id == 0:
        raise ValueError("Invalid user ID")
    return {"id": user_id, "name": "John Doe"}

# Sample calls
get_user_data(1)
get_user_data(0)  # This will fail and be logged

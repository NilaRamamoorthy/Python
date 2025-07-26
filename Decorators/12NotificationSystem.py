import functools

def notify(header="*** Notification Start ***", footer="*** Notification End ***"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(header)
            result = func(*args, **kwargs)
            print(footer)
            return result
        return wrapper
    return decorator

# Example function
@notify(header=">>> Start Message <<<", footer=">>> End Message <<<")
def send_message(name, message):
    print(f"{name}, you have a new message: {message}")
    return f"Message sent to {name}"

# Usage
result = send_message("Alice", "Your order has been shipped.")
print("Return Value:", result)

import functools

def call_counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' called {wrapper.call_count} times.")
        return func(*args, **kwargs)

    wrapper.call_count = 0

    def reset_count():
        wrapper.call_count = 0
        print(f"Call count for '{func.__name__}' has been reset.")

    wrapper.reset = reset_count
    return wrapper

# Example usage
@call_counter
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
greet.reset()  # Reset the counter
print(greet("Charlie"))

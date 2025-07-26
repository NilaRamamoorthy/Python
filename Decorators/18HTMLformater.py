import functools

def html_wrapper(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            return f"<{tag}>{content}</{tag}>"
        return wrapper
    return decorator

# Example: Chain decorators to simulate nested templates
@html_wrapper("div")
@html_wrapper("h2")
@html_wrapper("p")
def get_message():
    return "Welcome to our website!"

# Another example with different tag order
@html_wrapper("section")
@html_wrapper("h1")
def page_title():
    return "Smart Home Dashboard"

# Sample usage
print(get_message())
print(page_title())

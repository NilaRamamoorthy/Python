import functools
from datetime import datetime

# Simulated current user object
current_user = {
    "username": "john_doe",
    "role": "user"  # Change to "admin" to allow access
}

# Decorator factory
def access_control(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if current_user["role"] == required_role:
                print(f"[{datetime.now()}] Access granted to '{func.__name__}' for role '{current_user['role']}'")
                return func(*args, **kwargs)
            else:
                print(f"[{datetime.now()}] ACCESS DENIED: '{func.__name__}' requires role '{required_role}', but current role is '{current_user['role']}'")
        return wrapper
    return decorator

# Example usage
@access_control("admin")
def delete_user(user_id):
    print(f"User {user_id} deleted.")

# Sample calls
delete_user(101)  # Will be denied if role is not 'admin'

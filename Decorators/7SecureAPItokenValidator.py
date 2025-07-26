from functools import wraps

def validate_token(required_token):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = kwargs.get('token')
            if token != required_token:
                raise PermissionError("Invalid or missing API token.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage
@validate_token("secret_token")
def get_user_data(user_id, **kwargs):
    return f"Access granted to user data for user_id: {user_id}"

# Valid token test
try:
    print(get_user_data(101, token="secret_token"))
except PermissionError as e:
    print("Access Denied:", e)

# Invalid token test
try:
    print(get_user_data(102, token="wrong_token"))
except PermissionError as e:
    print("Access Denied:", e)

# Missing token test
try:
    print(get_user_data(103))
except PermissionError as e:
    print("Access Denied:", e)

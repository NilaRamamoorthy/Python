import functools

# Simulated user session
user = {
    "username": "nila",
    "is_logged_in": False
}

def require_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not user.get("is_logged_in"):
            raise PermissionError("Access denied: User is not logged in.")
        print(f"[Auth] Access granted to {user['username']}")
        return func(*args, **kwargs)
    return wrapper

# Example secured function
@require_login
def access_dashboard():
    return "Welcome to your dashboard!"

# Simulating login and access
try:
    print(access_dashboard())
except PermissionError as e:
    print(e)

# Simulate login
user["is_logged_in"] = True

# Try again after login
try:
    print(access_dashboard())
except PermissionError as e:
    print(e)

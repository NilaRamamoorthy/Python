# user_ops.py

# Simple set to store registered usernames
users: Set[str] = set()

def register_user(username: str):
    if username in users:
        print("Username already registered.")
    else:
        users.add(username)
        print(f"{username} registered successfully.")

def is_registered(username: str) -> bool:
    return username in users

# user_ops.py

users = set()

def register_user(username: str):
    if username in users:
        print(f"User '{username}' already exists.")
    else:
        users.add(username)
        print(f"User '{username}' registered successfully.")

def is_valid_user(username: str) -> bool:
    return username in users

def list_users():
    return list(users)

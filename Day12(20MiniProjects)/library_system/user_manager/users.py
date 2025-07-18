# users.py

# For this example, just track user names who issued books
issued_users = {}

def issue_to_user(user_id, user_name, isbn):
    if user_id in issued_users:
        print(f"User {user_name} already has a book issued.")
        return
    issued_users[user_id] = {
        "name": user_name,
        "isbn": isbn
    }
    print(f"Book issued to user '{user_name}'.")

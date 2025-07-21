from accounts import users

def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False

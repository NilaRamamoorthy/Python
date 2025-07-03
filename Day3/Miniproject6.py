# Login Authentication System
# Predefined credentials
stored_username = "admin"
stored_password = "1234"

# User input
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

# Validation using identity operators
if entered_username is stored_username and entered_password is stored_password:
    print("Login successful. Welcome!")
else:
    print("Login failed. Invalid username or password.")

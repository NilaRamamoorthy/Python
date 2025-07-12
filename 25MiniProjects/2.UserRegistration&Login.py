# User Registration and Login System

users = []  

# Function to register a new user
def register():
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    
    # Check if username already exists
    for user in users:
        if user['username'] == username:
            print("Username already taken.")
            return
    
    users.append({'username': username, 'password': password})
    print("Registration successful!")

# Function to login
def login():
    attempts = 3
    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        for user in users:
            if user['username'] == username and user['password'] == password:
                print(f"Welcome back, {username}!")
                return True
        attempts -= 1
        print(f"Invalid credentials. Attempts left: {attempts}")
    print("Too many failed login attempts.")
    return False

# Function to show all users (for admin/debug)
def show_users():
    print("\nRegistered Users:")
    if not users:
        print("No users yet.")
    for user in users:
        print(f"- {user['username']}")

# Main menu
def main_menu():
    while True:
        print("\n--- USER SYSTEM MENU ---")
        print("1. Register")
        print("2. Login")
        print("3. Show Users")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            show_users()
        elif choice == "4":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the program
main_menu()

# Username Availability Checker
# Predefined list of taken usernames
taken_usernames = ["admin", "john123", "user01", "ravi", "kavya"]

# Input: username to check
new_username = input("Enter desired username: ").strip().lower()

# Check availability using membership operator
if new_username in taken_usernames:
    print(f"The username '{new_username}' is already taken. Please choose another.")
else:
    print(f"The username '{new_username}' is available!")

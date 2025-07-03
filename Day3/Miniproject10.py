# Access Control Based on Role and ID
# Input
role = input("Enter your role (admin/user): ").strip().lower()
has_id = input("Do you have a valid ID? (yes/no): ").strip().lower()

# Access logic using nested if, and, not, in
valid_roles = ["admin", "user"]

if role in valid_roles:
    if has_id == "yes":
        print(f"Access granted to {role}.")
    else:
        print(f"Access denied. {role.capitalize()} must have a valid ID.")
else:
    print("Invalid role. Access denied.")

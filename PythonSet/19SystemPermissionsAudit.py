# Required permissions for a role
required_permissions = {"read", "write", "execute"}

# Permissions assigned to a user
user_permissions = {"read", "write"}  # 'execute' is missing

# Check if user has all required permissions
if user_permissions.issubset(required_permissions):
    print("User has valid permissions.")
else:
    print("User permissions are incomplete.")

# Identify missing permissions
missing = required_permissions.difference(user_permissions)
print("Missing Permissions:", missing)

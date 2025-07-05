# Bitwise Access Rights Checker

print("Permission Codes:")
print("1: Read")
print("2: Write")
print("4: Execute")

# Input: combined permission code (e.g., 3 = Read + Write)
permission = int(input("Enter permission code (e.g., 3 for Read + Write): "))

# Check permissions using bitwise AND &
has_read = permission & 1
has_write = permission & 2
has_execute = permission & 4

# Output result
print("\n--- Permission Details ---")
print(f"Read    : {' Yes' if has_read else ' No'}")
print(f"Write   : {' Yes' if has_write else ' No'}")
print(f"Execute : {' Yes' if has_execute else ' No'}")
print("-------------------------------")

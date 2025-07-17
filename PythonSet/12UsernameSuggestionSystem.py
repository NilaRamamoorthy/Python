# Already taken usernames
taken_usernames = {"alice123", "bob456", "charlie789"}

# New suggestions
new_suggestions = ["dave101", "alice123", "eve202", "bob456", "frank303"]

# Store valid, unique suggestions
valid_usernames = []

for username in new_suggestions:
    if username not in taken_usernames:
        taken_usernames.add(username)  # Add to taken list to avoid future reuse
        valid_usernames.append(username)
    else:
        print(f"'{username}' is already taken. Please choose another.")

print("\nAccepted New Usernames:", valid_usernames)
print("Updated Taken Usernames Set:", taken_usernames)

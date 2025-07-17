# List of emails with duplicates
email_list = [
    "alice@example.com", "bob@example.com", "charlie@example.com",
    "alice@example.com", "dave@example.com", "bob@example.com"
]

print("Original Email List:")
print(email_list)

# Remove duplicates by converting to a set
unique_emails = set(email_list)
print("\nUnique Emails (Set):")
print(unique_emails)

# Export back to list if needed
cleaned_email_list = list(unique_emails)
print("\nCleaned Email List:")
print(cleaned_email_list)

# Check if a particular email is in the cleaned list
check_email = "dave@example.com"
if check_email in unique_emails:
    print(f"\n{check_email} is in the contact list.")
else:
    print(f"\n{check_email} is NOT in the contact list.")

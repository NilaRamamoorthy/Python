# main.py

from generator import generate_password
from credentials import (
    add_credential, update_credential, delete_credential,
    search_by_site, search_by_tag
)

# Generate a secure password
generated_pass = generate_password(16)
print(f"Generated Password: {generated_pass}")

# Add credentials
add_credential("gmail.com", "user1", generated_pass, {"email", "personal"})
add_credential("github.com", "coder123", "gh@1234", {"dev", "code"})

# Update credential
update_credential("gmail.com", password="newsecurepass")

# Search by site
print("\nCredential for gmail.com:")
print(search_by_site("gmail.com"))

# Search by tag
print("\nSearch credentials tagged with 'dev':")
print(search_by_tag("dev"))

# Delete a credential
delete_credential("github.com")

# Final state
print("\nCredential for github.com after deletion:")
print(search_by_site("github.com"))

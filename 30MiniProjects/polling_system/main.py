# main.py

from user_ops import register_user, is_registered
from poll_ops import create_poll, vote, show_results

# Register users
register_user("alice")
register_user("bob")
register_user("alice")  # duplicate test

# Create poll
create_poll("Best Programming Language?", ["Python", "JavaScript", "C++", "Java"])

# Voting
if is_registered("alice"):
    vote("Best Programming Language?", "Python", "alice")

if is_registered("bob"):
    vote("Best Programming Language?", "JavaScript", "bob")

# Invalid vote (user already voted)
vote("Best Programming Language?", "C++", "alice")

# Invalid option
vote("Best Programming Language?", "Ruby", "bob")

# Show results
print("\nFinal Results:")
show_results("Best Programming Language?")

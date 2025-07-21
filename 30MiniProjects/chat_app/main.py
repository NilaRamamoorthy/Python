# main.py

from user_ops import register_user, is_valid_user, list_users
from chat_ops import send_message, view_chat, delete_chat

# Register users
register_user("alice")
register_user("bob")
register_user("charlie")

print("\nAll Registered Users:")
print(list_users())

# Send messages
if is_valid_user("alice") and is_valid_user("bob"):
    send_message("alice", "bob", "Hi Bob!")
    send_message("bob", "alice", "Hello Alice!")
    send_message("alice", "bob", "How are you?")

# View chat
view_chat("bob", "alice")

# Delete chat
delete_chat("alice", "bob")

# Try viewing again
view_chat("alice", "bob")

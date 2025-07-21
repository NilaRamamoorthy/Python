# chat_ops.py

from typing import Tuple, List, Dict

# (user1, user2) → list of messages
chat_logs: Dict[Tuple[str, str], List[str]] = {}

def _get_chat_key(user1: str, user2: str) -> Tuple[str, str]:
    return tuple(sorted((user1, user2)))

def send_message(sender: str, receiver: str, message: str):
    key = _get_chat_key(sender, receiver)
    if key not in chat_logs:
        chat_logs[key] = []
    chat_logs[key].append(f"{sender}: {message}")
    print("Message sent.")

def view_chat(user1: str, user2: str):
    key = _get_chat_key(user1, user2)
    if key in chat_logs:
        print(f"\nChat between {user1} and {user2}:")
        for msg in chat_logs[key]:
            print(msg)
    else:
        print("No messages found.")

def delete_chat(user1: str, user2: str):
    key = _get_chat_key(user1, user2)
    if key in chat_logs:
        del chat_logs[key]
        print(f"Chat between {user1} and {user2} deleted.")
    else:
        print("No chat to delete.")

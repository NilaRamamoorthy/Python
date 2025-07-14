import datetime

def chat_formatter(*messages):
    timestamp = datetime.datetime.now().strftime("[%H:%M]")
    formatted = list(map(lambda msg: f"{timestamp} {msg.capitalize()}", messages))
    return formatted

# Example Usage
chats = chat_formatter("hello", "how are you?", "let's meet at 5")
for chat in chats:
    print(chat)

# 19. Chat Conversation Logger
chats = [
    ('10:00', ('Alice', 'Hi')),
    ('10:01', ('Bob', 'Hello')),
    ('10:02', ('Alice', 'How are you?'))
]
for time, (sender, msg) in chats[-2:]:
    print(f"[{time}] {sender}: {msg}")
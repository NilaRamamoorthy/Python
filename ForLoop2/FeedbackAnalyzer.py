messages = [input("Enter feedback: ") for _ in range(3)]
for msg in messages:
    if "good" in msg.lower():
        print("Positive feedback")
    else:
        print("Neutral feedback")
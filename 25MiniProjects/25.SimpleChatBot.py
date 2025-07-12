# Simple Chatbot (Menu-Based)

def chatbot():
    print(" Simple Chatbot Ready! (type 'bye' to exit)\n")

    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! Need any assistance?",
        "what is your name?": "I'm PyBot, your simple chatbot.",
        "how are you?": "I'm just a bunch of code, but I'm functioning perfectly!",
        "bye": "Goodbye! Have a great day!",
    }

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "bye":
            print("Bot: " + responses["bye"])
            break
        elif user_input in responses:
            print("Bot: " + responses[user_input])
        else:
            print("Bot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()

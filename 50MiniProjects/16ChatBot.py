import json
import re
from functools import wraps

# --- Decorator to log chat ---  
def log_chat(func):
    @wraps(func)
    def wrapper(self, user_input):
        response = func(self, user_input)
        self.chat_history.append({'input': user_input, 'response': response})
        return response
    return wrapper

class UnknownQueryError(Exception):
    pass

class Chatbot:
    def __init__(self, responses_file):
        self.intents = {}  # keyword-pattern → response
        self.chat_history = []
        self.load_responses(responses_file)

    def load_responses(self, fname):
        """Load keyword responses from a JSON file."""
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                data = json.load(f)
            # Expecting format: { "hello": "Hello!", ... }
            for key, resp in data.items():
                pattern = re.compile(r'\b' + re.escape(key) + r'\b', re.IGNORECASE)
                self.intents[pattern] = resp
        except FileNotFoundError:
            raise FileNotFoundError(f"Responses file '{fname}' not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in responses file")

    @log_chat
    def get_response(self, user_input):
        """Case-insensitive keyword matching."""
        user_input = user_input.strip()
        if not user_input:
            raise UnknownQueryError("Empty input received")
        for pattern, resp in self.intents.items():
            if pattern.search(user_input):
                return resp
        raise UnknownQueryError("No matching response found")

    def possible_responses(self):
        """Generator yielding all defined responses."""
        for resp in self.intents.values():
            yield resp

    def chat(self):
        print("Chatbot is running. Type 'exit' to quit.")
        while True:
            user = input("You: ").strip()
            if user.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break
            try:
                reply = self.get_response(user)
            except UnknownQueryError:
                reply = "I'm sorry, I don't understand that."
            print("Chatbot:", reply)

    def save_chat(self, filename='chat_history.json'):
        """Optional: save history to JSON file."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.chat_history, f, indent=2)

if __name__ == "__main__":
    bot = Chatbot("responses.json")
    bot.chat()
    bot.save_chat()

import json
import time
from functools import wraps

# Decorator to time the quiz
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\n⏱️ Quiz completed in {round(end - start, 2)} seconds.")
        return result
    return wrapper

# Question class
class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer.upper()

    def ask(self):
        print("\n" + self.question)
        for opt in self.options:
            print(opt)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()
        while user_ans not in ['A', 'B', 'C', 'D']:
            print("❌ Invalid input. Choose A, B, C, or D.")
            user_ans = input("Your answer (A/B/C/D): ").strip().upper()
        return user_ans == self.answer

# Generator to yield questions
def load_questions(filename="questions.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for item in data:
                yield Question(item['question'], item['options'], item['answer'])
    except FileNotFoundError:
        print("❌ questions.json not found.")
        return
    except json.JSONDecodeError:
        print("❌ Error parsing the JSON file.")

# Start quiz
@timer
def start_quiz():
    print("🎮 Welcome to the Quiz Game!\n")
    score = 0
    total = 0

    for question in load_questions():
        if question.ask():
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong answer.")
        total += 1

    print(f"\n🎉 You scored {score} out of {total}.")

# Run the quiz
if __name__ == "__main__":
    start_quiz()

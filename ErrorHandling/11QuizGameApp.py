import logging

# Setup logging
logging.basicConfig(filename="quiz_exceptions.log", level=logging.ERROR, format="%(asctime)s - %(message)s")

# Custom exception
class InvalidAnswerError(Exception):
    pass

# Question bank
questions = [
    {"question": "What is the capital of France?", "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"], "answer": "A"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Mars", "C. Venus", "D. Saturn"], "answer": "B"},
    {"question": "What is the largest ocean?", "options": ["A. Atlantic", "B. Arctic", "C. Indian", "D. Pacific"], "answer": "D"},
]

score = 0

def ask_question(q):
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    try:
        user_input = input("Your answer (A/B/C/D): ").strip().upper()
        if user_input not in ['A', 'B', 'C', 'D']:
            raise InvalidAnswerError("Answer must be A, B, C, or D.")
        if user_input == q["answer"]:
            print("✅ Correct!")
            return 1
        else:
            print("❌ Wrong!")
            return 0
    except InvalidAnswerError as e:
        logging.error(f"Invalid input: {e}")
        print("Invalid choice. Please enter A, B, C, or D.")
        return 0
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("Something went wrong.")
        return 0

# Main quiz loop
print("=== Welcome to the Quiz Game ===")

for q in questions:
    score += ask_question(q)

print(f"\nYour final score is: {score}/{len(questions)}")

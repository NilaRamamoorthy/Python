import json
import time

QUESTION_FILE = 'questions.json'

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.load_questions()

    def load_questions(self):
        try:
            with open(QUESTION_FILE, 'r') as f:
                self.questions = json.load(f)
        except FileNotFoundError:
            print("Question bank not found, starting with empty bank.")
            self.questions = []

    def save_questions(self):
        with open(QUESTION_FILE, 'w') as f:
            json.dump(self.questions, f, indent=2)

    def add_question(self):
        print("Add a new question")
        qtype = input("Type (mcq/truefalse): ").strip().lower()
        question = input("Question text: ")
        difficulty = input("Difficulty (easy/medium/hard): ").lower()
        if qtype == 'mcq':
            options = []
            for i in range(4):
                opt = input(f"Option {i+1}: ")
                options.append(opt)
            answer = input("Correct option number (1-4): ")
            try:
                answer = int(answer) - 1
            except:
                print("Invalid answer number")
                return
            self.questions.append({
                "type": "mcq",
                "question": question,
                "options": options,
                "answer": answer,
                "difficulty": difficulty
            })
        elif qtype == 'truefalse':
            answer = input("Answer (true/false): ").strip().lower()
            if answer not in ['true', 'false']:
                print("Invalid answer")
                return
            self.questions.append({
                "type": "truefalse",
                "question": question,
                "answer": answer,
                "difficulty": difficulty
            })
        else:
            print("Unsupported question type")
            return
        self.save_questions()
        print("Question added.")

    def start_quiz(self, difficulty=None, time_limit=None):
        print("Starting quiz...")
        filtered = [q for q in self.questions if (difficulty is None or q['difficulty'] == difficulty)]
        if not filtered:
            print("No questions found for the selected difficulty.")
            return

        self.score = 0
        start_time = time.time()
        for idx, q in enumerate(filtered, 1):
            if time_limit and (time.time() - start_time) > time_limit:
                print("\nTime's up!")
                break

            print(f"\nQ{idx}: {q['question']}")
            if q['type'] == 'mcq':
                for i, opt in enumerate(q['options']):
                    print(f"  {i+1}. {opt}")
                ans = input("Your answer (1-4): ")
                if ans.isdigit() and int(ans) - 1 == q['answer']:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! Correct answer: {q['options'][q['answer']]}")
            elif q['type'] == 'truefalse':
                ans = input("Your answer (true/false): ").strip().lower()
                if ans == q['answer']:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! Correct answer: {q['answer']}")
            else:
                print("Unknown question type.")

        print(f"\nQuiz finished! Your score: {self.score} / {len(filtered)}")

def main():
    quiz = Quiz()
    print("Quiz Application")

    while True:
        print("\nMenu:")
        print("1. Take Quiz")
        print("2. Add Question")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            diff = input("Select difficulty (easy/medium/hard) or leave blank for all: ").lower() or None
            time_limit_str = input("Set time limit in seconds (0 for no limit): ")
            try:
                time_limit = int(time_limit_str)
                if time_limit == 0:
                    time_limit = None
            except ValueError:
                time_limit = None
            quiz.start_quiz(diff, time_limit)

        elif choice == '2':
            quiz.add_question()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

from quiz.questions import load_questions
from quiz.evaluate import evaluate_answers
from quiz.score import display_score

def start_quiz():
    name = input("Enter your name: ")
    questions = load_questions()
    user_answers = []

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for opt in q['options']:
            print(f" - {opt}")
        ans = input("Your answer: ")
        user_answers.append(ans)

    correct = evaluate_answers(questions, user_answers)
    display_score(name, len(questions), correct)

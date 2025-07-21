from question_bank import get_random_question, get_all_topics
import random

score = 0
asked = set()

def ask_question():
    global score
    q = get_random_question()
    while q["question"] in asked:
        q = get_random_question()
    asked.add(q["question"])

    print(f"\nQ: {q['question']}")
    for idx, opt in enumerate(q["options"], 1):
        print(f"{idx}. {opt}")
    ans = input("Enter your choice (1-4): ")

    if ans.isdigit() and 1 <= int(ans) <= 4:
        selected = q["options"][int(ans) - 1]
        if selected == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {q['answer']}")
    else:
        print("⚠️ Invalid input.")

def show_result():
    print(f"\n🎯 Final Score: {score}/{len(asked)}")
    print(f"📚 Topics Covered: {', '.join(get_all_topics())}")

# Quiz data
quiz = {
    "What is the capital of India?": {
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    "What is 2 + 2?": {
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    "Which language is used for web development?": {
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    }
}

# Store user answers
user_answers = {}

# Loop through quiz
for question, data in quiz.items():
    print(f"\n{question}")
    for i, opt in enumerate(data["options"], 1):
        print(f"{i}. {opt}")
    
    choice = int(input("Enter option number: "))
    selected = data["options"][choice - 1]
    user_answers[question] = selected

# Score summary
correct = {q: a for q, a in user_answers.items() if a == quiz[q]["answer"]}
wrong = {q: a for q, a in user_answers.items() if a != quiz[q]["answer"]}

print(f"\nTotal Questions: {len(quiz)}")
print(f"Correct Answers: {len(correct)}")
print(f"Wrong Answers: {len(wrong)}")

# Show correct vs wrong
print("\nCorrectly Answered:")
for q in correct:
    print(q)

print("\nWrongly Answered:")
for q in wrong:
    print(f"{q} (Your answer: {wrong[q]}, Correct: {quiz[q]['answer']})")

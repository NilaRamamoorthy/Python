questions = [
    ("Capital of India?", "delhi"),
    ("5 + 3 = ?", "8"),
    ("Python keyword for loop?", "for"),
    ("Sun rises in the ___?", "east"),
    ("2 x 2 = ?", "4")
]

for q, ans in questions:
    user_ans = input(q + " ")
    if user_ans.lower() != ans:
        print("Wrong answer. Game Over.")
        break
else:
    print("Quiz Completed!")

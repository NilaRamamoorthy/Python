# Quiz Answer Tracker

# Correct answers for the quiz
correct_answers = ["A", "C", "B", "D", "A"]

# User's answers list
user_answers = []

# Take answers from the user
print("Enter your answers for 5 questions (A/B/C/D):")
for i in range(5):
    ans = input(f"Question {i+1}: ").strip().upper()
    user_answers.append(ans)

# Compare answers
score = 0
for i in range(5):
    if user_answers[i] == correct_answers[i]:
        score += 1

# Display results
print("\nYour Answers:", user_answers)
print("Correct Answers:", correct_answers)
print(f"Total Correct: {score}")
print(f"Total Incorrect: {5 - score}")
print(f"Percentage: {(score / 5) * 100}%")

# 20. Quiz Grader App
correct_answers = ['A', 'B', 'C', 'D', 'A']
user_answers = [input(f"Answer for Q{i+1}: ").upper() for i in range(5)]
score = 0
for c, u in zip(correct_answers, user_answers):
    if c == u:
        score += 1

if score >= 5:
    grade = "A"
elif score == 4:
    grade = "B"
elif score == 3:
    grade = "C"
else:
    grade = "D"

print(f"Score: {score}/5, Grade: {grade}")
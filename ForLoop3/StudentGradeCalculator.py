#1. Student Grade Calculator
name = input("Enter student name: ")
marks = [float(input(f"Enter mark {i+1}: ")) for i in range(5)]
total = sum(marks)
avg = total / 5

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
else:
    grade = 'D'

print(f"{name}'s Grade: {grade}")
name = input("Enter student name: ")
student_class = input("Enter class: ")
marks = []

for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
else:
    grade = 'D'

print(f"\nReport Card for {name} (Class {student_class})")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
# Student Grade Evaluator
# Input
name = input("Enter student name: ").strip().title()

print("Enter marks for 5 subjects:")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

# Arithmetic: Calculate average
total = m1 + m2 + m3 + m4 + m5
average = total / 5

# Determine grade using comparison and logical operators
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

# Display result using f-strings
print("\n--- Student Report ---")
print(f"Name       : {name}")
print(f"Average    : {average:.2f}")
print(f"Grade      : {grade}")
print("------------------------")

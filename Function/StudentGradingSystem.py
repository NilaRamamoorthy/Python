# Function to calculate average and grade
def evaluate_student(name, marks):
    # Check for any failing mark (< 35)
    if any(mark < 35 for mark in marks):
        print(f"\n{name} has failed in one or more subjects.")
        print("Please re-enter marks for re-evaluation.")
        new_marks = []
        for i in range(5):
            new_mark = int(input(f"Enter new mark for Subject {i+1}: "))
            new_marks.append(new_mark)
        # Recursive call for re-evaluation
        return evaluate_student(name, new_marks)

    # Calculate average
    avg = sum(marks) / len(marks)

    # Grade logic
    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "D"

    return avg, grade

# Sample usage
name = input("Enter Student Name: ")
marks = []
for i in range(5):
    m = int(input(f"Enter mark for Subject {i+1}: "))
    marks.append(m)

average, grade = evaluate_student(name, marks)
print(f"\n{name}'s Result:")
print(f"Average: {average}")
print(f"Grade: {grade}")

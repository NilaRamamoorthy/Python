def get_marks():
    print("Enter marks for 5 subjects:")
    marks = []
    for i in range(1, 6):
        score = int(input(f"Subject {i}: "))
        marks.append(score)

    # Check for any failed subject
    if any(mark < 35 for mark in marks):
        print(" Some marks are below 35. Re-evaluation needed.")
        return get_marks()  

    return marks

def calculate_grade(marks):
    avg = sum(marks) / len(marks)
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

# --- Example Usage ---
marks = get_marks()
average, grade = calculate_grade(marks)

print(f"\n✅ Final Report:")
print(f"Marks: {marks}")
print(f"Average: {average}")
print(f"Grade: {grade}")

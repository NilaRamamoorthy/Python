# Student Grading System

def input_marks():
    marks = []
    for i in range(1, 6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return marks

def calculate_grade(marks):
    if any(m < 35 for m in marks):
        print("Some marks are below passing. Please re-enter.")
        return calculate_grade(input_marks())  # Recursion for re-evaluation

    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "E"
    
    return avg, grade

# Example usage
student_marks = input_marks()
average, grade = calculate_grade(student_marks)
print(f"Average: {average}, Grade: {grade}")

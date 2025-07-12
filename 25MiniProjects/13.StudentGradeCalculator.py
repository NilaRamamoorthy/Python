# Student Grade Calculator

students = []

# Function to calculate average and grade
def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        grade = 'A+'
    elif average >= 75:
        grade = 'A'
    elif average >= 60:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return average, grade

# Main function
def student_grade_calculator():
    print("Student Grade Calculator")
    while True:
        name = input("\nEnter student name (or type 'exit' to stop): ").strip().title()
        if name.lower() == "exit":
            break

        marks = []
        for i in range(1, 6):
            while True:
                try:
                    mark = float(input(f"Enter mark for subject {i}: "))
                    marks.append(mark)
                    break
                except ValueError:
                    print("Please enter a valid number.")

        avg, grade = calculate_grade(marks)
        students.append({"name": name, "marks": marks, "average": avg, "grade": grade})
        print(f"\n{name}'s Average: {avg:.2f}")
        print(f"{name}'s Grade: {grade}")

    print("\nAll Students Summary:")
    for student in students:
        print(f"{student['name']} → Avg: {student['average']:.2f}, Grade: {student['grade']}")

# Run the app
student_grade_calculator()

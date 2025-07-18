# grade_utils.py

# Set of valid subjects
valid_subjects = {"Math", "Science", "English", "History", "Computer"}

# Dictionary to store marks: (student_id,) -> subject marks
student_marks = {}

def add_student_marks(student_id, name, marks_dict):
    key = (student_id,)
    if key in student_marks:
        print(f"Marks for student ID {student_id} already recorded.\n")
        return

    # Validate subjects
    subject_set = set(marks_dict.keys())
    if not subject_set.issubset(valid_subjects):
        print("Invalid subject(s) found in marks entry.\n")
        return

    student_marks[key] = {
        "name": name,
        "marks": marks_dict
    }
    print(f"Marks added for student '{name}'.\n")

def calculate_grade(marks_dict):
    total = sum(marks_dict.values())
    avg = total / len(marks_dict)
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 45:
        return "C"
    else:
        return "F"

def view_grades():
    print("\nStudent Grade Report:")
    for student_id, data in student_marks.items():
        grade = calculate_grade(data["marks"])
        print(f"Student ID: {student_id}, Name: {data['name']}, Grade: {grade}")

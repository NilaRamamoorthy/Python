def get_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 75:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 40:
        return 'D'
    else:
        return 'F'

def convert_marks_to_grades(marks):
    grades = list(map(get_grade, marks))
    return grades

# Example Usage
marks_input = input("Enter marks separated by space: ")
marks_list = list(map(int, marks_input.strip().split()))

graded_list = convert_marks_to_grades(marks_list)
print("Grades:", graded_list)

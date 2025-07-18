# main.py

from grade_utils import add_student_marks, view_grades

# Add student marks
add_student_marks(301, "Alice", {"Math": 85, "Science": 90, "English": 88})
add_student_marks(302, "Bob", {"Math": 60, "History": 55, "Computer": 70})
add_student_marks(301, "Alice", {"Math": 95})  # Duplicate
add_student_marks(303, "Carol", {"Math": 100, "Dance": 90})  # Invalid subject

# View grades
view_grades()

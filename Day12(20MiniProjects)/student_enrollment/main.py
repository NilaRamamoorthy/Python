# main.py

from student_utils import enroll_student, add_course, view_student

# Dictionary to hold student data
students = {}

# Add students
enroll_student(students, (101,), "Alice")
enroll_student(students, (102,), "Bob")

# Enroll in courses
add_course(students, (101,), "Math")
add_course(students, (101,), "Science")
add_course(students, (102,), "Math")
add_course(students, (102,), "Math")  # duplicate

# View student details
view_student(students, (101,))
view_student(students, (102,))

# Students enrolled in Python course
python_students = {"Alice", "Bob", "Charlie", "David", "Eva"}

# Students enrolled in Java course
java_students = {"Charlie", "Eva", "Frank", "George", "Helen"}

# Students enrolled in both courses
both_courses = python_students.intersection(java_students)
print("Students in both Python and Java:", both_courses)

# Students only in Python
only_python = python_students.difference(java_students)
print("Students only in Python:", only_python)

# All students from both courses
all_students = python_students.union(java_students)
print("All students (Python or Java):", all_students)

# Students enrolled in only one course
only_one_course = python_students.symmetric_difference(java_students)
print("Students in only one course:", only_one_course)

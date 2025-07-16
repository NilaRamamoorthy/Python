# Initial registrations
registrations = {
    "Alice": ["Math", "English"],
    "Bob": ["Science"],
    "Charlie": ["Math", "Science"]
}

# 1. Add a course
def add_course(student, course):
    if student in registrations:
        if course not in registrations[student]:
            registrations[student].append(course)
    else:
        registrations[student] = [course]

# 2. Drop a course
def drop_course(student, course):
    if student in registrations and course in registrations[student]:
        registrations[student].remove(course)

# 3. Show all students in a course
def list_students_in_course(course):
    print(f"Students enrolled in {course}:")
    for student, courses in registrations.items():
        if course in courses:
            print(student)

# Perform operations
add_course("Bob", "English")
drop_course("Charlie", "Science")
list_students_in_course("Math")

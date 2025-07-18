# student_utils.py

available_courses = {"Math", "Science", "History", "English", "Computer"}

def enroll_student(student_db, student_id, name):
    if student_id in student_db:
        print(f"Student ID {student_id} already exists.")
        return
    student_db[student_id] = {
        "name": name,
        "courses": set()
    }
    print(f"Student '{name}' enrolled successfully.")

def add_course(student_db, student_id, course):
    if course not in available_courses:
        print(f"Course '{course}' is not available.")
        return
    if student_id not in student_db:
        print("Student ID not found.")
        return
    if course in student_db[student_id]["courses"]:
        print(f"Student already enrolled in '{course}'.")
    else:
        student_db[student_id]["courses"].add(course)
        print(f"Course '{course}' added for student {student_id}.")

def view_student(student_db, student_id):
    if student_id in student_db:
        data = student_db[student_id]
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {data['name']}")
        print(f"Courses Enrolled: {', '.join(data['courses']) if data['courses'] else 'None'}")
    else:
        print("Student ID not found.")

from student_tracker.database import load_data, save_data

def add_course(course_id, course_name):
    data = load_data()
    if course_id not in data["courses"]:
        data["courses"][course_id] = {"name": course_name}
        save_data(data)
        print(f"Course {course_name} added.")
    else:
        print("Course already exists.")

def enroll_student(student_id, course_id):
    data = load_data()
    if student_id in data["students"] and course_id in data["courses"]:
        if course_id not in data["students"][student_id]["courses"]:
            data["students"][student_id]["courses"].append(course_id)
            save_data(data)
            print("Student enrolled in course.")
        else:
            print("Student already enrolled in this course.")
    else:
        print("Invalid student or course ID.")

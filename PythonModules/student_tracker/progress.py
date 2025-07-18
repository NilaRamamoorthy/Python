from student_tracker.database import load_data

def view_student_progress(student_id):
    data = load_data()
    if student_id in data["students"]:
        student = data["students"][student_id]
        print(f"\nProgress for {student['name']}:")
        for course_id in student["courses"]:
            course_name = data["courses"].get(course_id, {}).get("name", "Unknown")
            print(f"- {course_id}: {course_name}")
    else:
        print("Student not found.")

from student_tracker.database import load_data, save_data

def add_student(student_id, name):
    data = load_data()
    if student_id not in data["students"]:
        data["students"][student_id] = {"name": name, "courses": []}
        save_data(data)
        print(f"Student {name} added.")
    else:
        print("Student already exists.")

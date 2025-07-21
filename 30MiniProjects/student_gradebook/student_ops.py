import json

DATA_FILE = "gradebook.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_student():
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    student = (roll, name)
    grades = {}
    subjects = input("Enter subjects (comma-separated): ").split(",")
    for sub in subjects:
        sub = sub.strip()
        mark = int(input(f"Enter marks for {sub}: "))
        grades[sub] = mark
    data = load_data()
    data.append({"student": student, "grades": grades})
    save_data(data)
    print("Student added!")

def update_grades():
    roll = int(input("Enter student roll number: "))
    data = load_data()
    for entry in data:
        if entry["student"][0] == roll:
            subject = input("Enter subject to update: ")
            mark = int(input("Enter new mark: "))
            entry["grades"][subject] = mark
            save_data(data)
            print("Grade updated.")
            return
    print("Student not found.")

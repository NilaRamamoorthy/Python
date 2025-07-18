import json

def register_student(name, grade):
    student = {"name": name, "grade": grade}
    
    try:
        with open("students.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(student)

    with open("students.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Student '{name}' registered.")

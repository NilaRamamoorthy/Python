import json

def register_teacher(name, subject):
    teacher = {"name": name, "subject": subject}
    
    try:
        with open("teachers.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(teacher)

    with open("teachers.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Teacher '{name}' registered.")

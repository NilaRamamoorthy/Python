import json

def assign_subject(subject, teacher):
    assignment = {"subject": subject, "teacher": teacher}

    try:
        with open("subjects.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(assignment)

    with open("subjects.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Assigned subject '{subject}' to teacher '{teacher}'.")

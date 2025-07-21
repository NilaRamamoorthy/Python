from student_ops import load_data

def calculate_average(grades):
    return sum(grades.values()) / len(grades)

def display_all_reports():
    data = load_data()
    print("\n--- Student Report Cards ---")
    for entry in data:
        student = entry["student"]
        grades = entry["grades"]
        avg = calculate_average(grades)
        print(f"\nRoll No: {student[0]}, Name: {student[1]}")
        for subject, mark in grades.items():
            print(f"{subject}: {mark}")
        print(f"Average: {avg:.2f}")

def top_performers():
    data = load_data()
    scored = [(entry["student"], sum(entry["grades"].values())) for entry in data]
    scored.sort(key=lambda x: x[1], reverse=True)
    print("\n--- Top Performers ---")
    for student, total in scored[:3]:
        print(f"{student[1]} (Roll: {student[0]}) - Total: {total}")

from students.register import register_student
from teachers.register import register_teacher
from subjects.assign import assign_subject
import json

def view_all_data():
    print("\n--- Student Data ---")
    try:
        with open("students.json") as f:
            print(json.dumps(json.load(f), indent=2))
    except:
        print("No student data.")

    print("\n--- Teacher Data ---")
    try:
        with open("teachers.json") as f:
            print(json.dumps(json.load(f), indent=2))
    except:
        print("No teacher data.")

    print("\n--- Subject Assignments ---")
    try:
        with open("subjects.json") as f:
            print(json.dumps(json.load(f), indent=2))
    except:
        print("No subject assignments.")

if __name__ == "__main__":
    while True:
        print("\n1. Register Student\n2. Register Teacher\n3. Assign Subject\n4. View All Data\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Student name: ")
            grade = input("Grade: ")
            register_student(name, grade)
        elif choice == "2":
            name = input("Teacher name: ")
            subject = input("Subject: ")
            register_teacher(name, subject)
        elif choice == "3":
            subject = input("Subject: ")
            teacher = input("Teacher name: ")
            assign_subject(subject, teacher)
        elif choice == "4":
            view_all_data()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

# main.py

from student_data import students
from attendance_ops import mark_attendance, view_attendance_by_date, view_attendance_by_student, get_absentees

# Sample attendance storage
attendance_data = {}

# Convert student list to set of roll numbers
all_student_rolls = {roll for roll, _ in students}

def display_menu():
    print("\n--- Attendance Management System ---")
    print("1. Mark Attendance")
    print("2. View Attendance by Date")
    print("3. View Attendance by Student")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        present_rolls = input("Enter present student roll numbers (comma-separated): ")
        present_list = [int(r.strip()) for r in present_rolls.split(",") if r.strip().isdigit()]
        mark_attendance(attendance_data, present_list)

    elif choice == "2":
        date_query = input("Enter date (YYYY-MM-DD): ")
        view_attendance_by_date(attendance_data, students, date_query)

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        if roll.isdigit():
            view_attendance_by_student(attendance_data, int(roll))
        else:
            print("Invalid roll number.")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

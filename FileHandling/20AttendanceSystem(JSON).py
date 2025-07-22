import json
import os
from datetime import datetime

ATTENDANCE_FILE = "attendance.json"

def load_attendance():
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_attendance(data):
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def mark_attendance():
    name = input("Enter student name: ").strip()
    date = datetime.today().strftime("%Y-%m-%d")
    data = load_attendance()
    
    if name in data:
        data[name].append(date)
    else:
        data[name] = [date]
    
    save_attendance(data)
    print(f"Attendance marked for {name} on {date}.")

def view_attendance():
    data = load_attendance()
    if not data:
        print("No attendance records.")
        return
    
    print("\nAttendance Records:")
    for name, dates in data.items():
        print(f"{name}: {', '.join(dates)}")

def view_student_attendance():
    name = input("Enter student name to view attendance: ").strip()
    data = load_attendance()
    if name in data:
        print(f"{name}: {', '.join(data[name])}")
    else:
        print(f"No records found for {name}.")

def main():
    while True:
        print("\n--- Attendance System ---")
        print("1. Mark Attendance")
        print("2. View All Attendance")
        print("3. View Specific Student Attendance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            view_student_attendance()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

main()

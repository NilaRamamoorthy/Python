import csv
from datetime import datetime
import os

ATTENDANCE_FILE = "attendance.csv"

def mark_attendance(name):
    now = datetime.now()
    entry = [name, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")]

    with open(ATTENDANCE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(entry)
    print(f"Attendance marked for {name}")

def view_attendance(name=None):
    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance records found.")
        return

    with open(ATTENDANCE_FILE, "r") as file:
        reader = csv.reader(file)
        print(f"{'Name':<15} {'Date':<12} {'Time':<10}")
        print("-" * 40)
        for row in reader:
            if name is None or row[0].lower() == name.lower():
                print(f"{row[0]:<15} {row[1]:<12} {row[2]:<10}")

def main():
    while True:
        print("\n1. Mark Attendance\n2. View Attendance\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            mark_attendance(name)
        elif choice == "2":
            name = input("Enter employee name (leave blank to show all): ").strip()
            view_attendance(name if name else None)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

main()

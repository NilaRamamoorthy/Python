import csv
import os

FILENAME = "student_marks.csv"

def add_student(name, roll, marks):
    file_exists = os.path.isfile(FILENAME)
    with open(FILENAME, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Roll", "Marks"])
        writer.writerow([name, roll, marks])
    print("Student record added.")

def view_all_students():
    if not os.path.exists(FILENAME):
        print("No student records found.")
        return
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def calculate_average_and_topper():
    if not os.path.exists(FILENAME):
        print("No data to process.")
        return

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        total = 0
        count = 0
        topper = None
        top_marks = -1
        for row in reader:
            marks = int(row["Marks"])
            total += marks
            count += 1
            if marks > top_marks:
                top_marks = marks
                topper = row["Name"]
        if count > 0:
            print(f"Average Marks: {total / count}")
            print(f"Topper: {topper} with {top_marks} marks")
        else:
            print("No student data available.")

# Demo usage
add_student("Alice", "101", 89)
add_student("Bob", "102", 95)
view_all_students()
calculate_average_and_topper()

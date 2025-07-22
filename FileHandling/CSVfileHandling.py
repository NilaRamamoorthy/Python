import csv

# 31. Create a CSV file containing student names and marks
def create_student_csv(filename):
    students = [
        ["Name", "Marks"],
        ["Alice", 85],
        ["Bob", 78],
        ["Charlie", 92],
        ["Daisy", 67],
        ["Ethan", 88]
    ]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students)
    print(f"{filename} created.")

# Demo
create_student_csv("students.csv")


# 32. Read CSV and print names of students who scored >80
def print_high_scorers(filename):
    print("Students who scored more than 80:")
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["Marks"]) > 80:
                print(row["Name"])

# Demo
print_high_scorers("students.csv")


# 33. Append new student data to the CSV file
def append_student(filename, name, marks):
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, marks])
    print(f"Appended: {name}, {marks}")

# Demo
append_student("students.csv", "Fiona", 95)
append_student("students.csv", "George", 74)


# 34. Read CSV and convert to dictionary {name: marks}
def csv_to_dict(filename):
    student_dict = {}
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student_dict[row["Name"]] = int(row["Marks"])
    print("Student Dictionary:", student_dict)
    return student_dict

# Demo
csv_to_dict("students.csv")


# 35. Summary: Highest and average marks
def student_summary(filename):
    marks = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks.append(int(row["Marks"]))
    if marks:
        print(f"Highest Marks: {max(marks)}")
        print(f"Average Marks: {sum(marks)/len(marks):.2f}")
    else:
        print("No student data found.")

# Demo
student_summary("students.csv")

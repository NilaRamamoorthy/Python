# Initial attendance data
attendance = {
    "2025-07-14": ["Alice", "Bob"],
    "2025-07-15": ["Alice", "Charlie"],
    "2025-07-16": ["Bob", "Charlie"]
}

# 1. Add attendance for a new day
attendance["2025-07-17"] = ["Alice", "Bob", "Charlie"]

# 2. Mark absentees
def find_absentees(date, all_students):
    present = attendance.get(date, [])
    return [student for student in all_students if student not in present]

all_students = ["Alice", "Bob", "Charlie", "David"]
absentees = find_absentees("2025-07-15", all_students)
print(f"Absentees on 2025-07-15: {absentees}")

# 3. List all attendance dates
print("\nDates with attendance recorded:")
for date in attendance.keys():
    print(date)

# 4. Reverse query: attendance count per student
student_attendance = {}
for date, present_list in attendance.items():
    for student in present_list:
        student_attendance[student] = student_attendance.get(student, 0) + 1

print("\nTotal Days Present per Student:")
for student, count in student_attendance.items():
    print(f"{student}: {count} day(s)")

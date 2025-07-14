# Class Attendance System

# Master list of students
master_list = ["Asha", "Ravi", "Kiran", "Meena", "Ravi", "Asha"]

# Remove duplicates using set and sort
unique_students = sorted(list(set(master_list)))

# Present students marked today
present_students = []

print("Enter names of present students (type 'done' to finish):")
while True:
    name = input("Present student: ").strip().title()
    if name.lower() == "done":
        break
    if name in unique_students and name not in present_students:
        present_students.append(name)
    elif name not in unique_students:
        print("Name not in master list.")
    else:
        print("Already marked present.")

# Count absentees
absent_students = [s for s in unique_students if s not in present_students]

# Summary
print("\nPresent Students:", present_students)
print("Absent Students:", absent_students)
print(f"Total Present: {len(present_students)}")
print(f"Total Absent: {len(absent_students)}")

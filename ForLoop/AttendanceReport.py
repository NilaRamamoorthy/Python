students = input("Enter student names separated by commas: ").split(",")
for i, student in enumerate(students, start=101):
    print(f"{i}. {student.strip()} - Present")

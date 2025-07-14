# Student Score Tracker

# Initial list of students with their marks
students = [["Ram", 85], ["Sam", 78], ["Ravi", 92]]

# Display all students and scores
print("Student Scores:")
for s in students:
    print(f"{s[0]} scored {s[1]}")

# Add a new student
students.append(["Anjali", 88])
print("\nAfter adding Anjali:", students)

# Update Sam's marks
for s in students:
    if s[0] == "Sam":
        s[1] = 81
print("\nAfter updating Sam's marks:", students)

# Remove a student
students.remove(["Ram", 85])
print("\nAfter removing Ram:", students)

# Sort students alphabetically by name
students.sort(key=lambda x: x[0])
print("\nSorted by name:", students)

# Analyze scores
marks = [s[1] for s in students]
print("\n Highest Score:", max(marks))
print(" Lowest Score:", min(marks))

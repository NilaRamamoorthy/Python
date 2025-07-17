# List of enrolled students
enrolled_students = {"Alice", "Bob", "Charlie", "David", "Eva"}

# Students who are present today
present_students = {"Alice", "Charlie", "Eva"}

# Find absent students using set difference
absent_students = enrolled_students.difference(present_students)
print("Absent Students:", absent_students)

# Latecomers arriving after attendance taken
latecomers = {"David"}

# Add latecomers to present list
present_students.update(latecomers)
print("Updated Present Students:", present_students)

# Recalculate absentees
absent_students = enrolled_students.difference(present_students)
print("Final Absentees After Including Latecomers:", absent_students)

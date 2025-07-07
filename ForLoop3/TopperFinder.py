#  15. Topper Finder in a Class
students = {"Ravi": 88, "Nila": 92, "Kiran": 85}
topper = max(students, key=students.get)
print(f"Topper: {topper} with {students[topper]} marks")
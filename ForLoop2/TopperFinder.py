students = {"Asha": 89, "Ravi": 93, "Nila": 88}
topper = max(students, key=students.get)
print(f"Topper: {topper} with {students[topper]} marks")
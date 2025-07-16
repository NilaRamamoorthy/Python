# Initial data
students = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 70, "Science": 60},
}

# 1. Add new student
students["Charlie"] = {"Math": 88, "Science": 92}

# 2. Add new subject to existing student
students["Bob"]["English"] = 75

# 3. Update mark
students["Alice"]["Math"] = 95

# 4. Remove subject
students["Charlie"].pop("Science", None)

# 4. Remove student
students.pop("Bob", None)

# 5. Display all students with average marks
print("\n--- Student Averages ---")
for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    print(f"{name}: {avg:.2f}")

# 6. Identify topper
topper = max(students, key=lambda name: sum(students[name].values()))
print(f"\n🏆 Topper: {topper}")

# 7. Handle missing data
print("\nCharlie's English mark:", students.get("Charlie", {}).get("English", "Not Available"))

# 8. Passed students (avg > 50)
passed = {name: avg for name, subjects in students.items()
          if (avg := sum(subjects.values()) / len(subjects)) > 50}

print("\nPassed Students:")
for name, avg in passed.items():
    print(f"{name}: {avg:.2f}")

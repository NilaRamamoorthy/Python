import csv
from functools import wraps

# ========== Decorator: Memoization ==========
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(self):
        if self.id not in cache:
            cache[self.id] = func(self)
        return cache[self.id]
    return wrapper

# ========== OOP: Student Class ==========
class Student:
    def __init__(self, id, name, marks: dict):
        self.id = id
        self.name = name
        self.marks = marks  # subject → mark

    @memoize
    def calculate_gpa(self):
        total = 0
        count = 0
        for mark in self.marks.values():
            total += mark
            count += 1
        return round(total / count, 2) if count else 0

    def assign_grade(self):
        gpa = self.calculate_gpa()
        if gpa >= 90:
            return 'A'
        elif gpa >= 80:
            return 'B'
        elif gpa >= 70:
            return 'C'
        elif gpa >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return f"{self.id} - {self.name} | GPA: {self.calculate_gpa()} | Grade: {self.assign_grade()}"

# ========== Main Logic ==========
class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self):
        try:
            sid = input("Enter Student ID: ").strip()
            if sid in self.students:
                print("Student ID already exists.")
                return
            name = input("Enter Name: ").strip()
            marks = {}
            subjects = input("Enter subjects separated by comma: ").split(",")
            for subject in subjects:
                subject = subject.strip()
                mark = float(input(f"Enter marks for {subject}: "))
                if not (0 <= mark <= 100):
                    raise ValueError(f"Invalid mark for {subject}. Must be 0–100.")
                marks[subject] = mark
            self.students[sid] = Student(sid, name, marks)
            print("[+] Student added.")
        except ValueError as e:
            print(f"[!] Error: {e}")

    def display_students(self):
        if not self.students:
            print("No students to display.")
            return
        print("\n-- Student List --")
        for student in self.students.values():
            print(student)

    def class_average(self):
        if not self.students:
            return 0
        total = sum(s.calculate_gpa() for s in self.students.values())
        avg = total / len(self.students)
        print(f"\n[📊] Class Average GPA: {round(avg, 2)}")

    def top_student(self):
        if not self.students:
            print("No students.")
            return
        top = max(self.students.values(), key=lambda s: s.calculate_gpa())
        print(f"\n[🏆] Top Student:\n{top}")

    def unique_subjects(self):
        subjects = set()
        for s in self.students.values():
            subjects.update(s.marks.keys())
        print("\n[📚] Unique Subjects:", ", ".join(subjects))

    def export_to_csv(self, filename="student_grades.csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "GPA", "Grade"])
            for student in self.students.values():
                writer.writerow([student.id, student.name, student.calculate_gpa(), student.assign_grade()])
        print(f"[💾] Exported to {filename}")

    def grade_a_students(self):
        print("\n[🎖️] Students with Grade A:")
        for student in self._generate_a_students():
            print(student)

    def _generate_a_students(self):
        return (s for s in self.students.values() if s.assign_grade() == 'A')

# ========== Menu ==========
def main():
    sm = StudentManager()

    menu = """
-- Student Grade System --
1. Add Student
2. Show All Students
3. Show Class Average
4. Show Top Student
5. Show Unique Subjects
6. Show Grade A Students
7. Export to CSV
8. Exit
"""

    while True:
        print(menu)
        choice = input("Enter choice: ").strip()

        if choice == "1":
            sm.add_student()
        elif choice == "2":
            sm.display_students()
        elif choice == "3":
            sm.class_average()
        elif choice == "4":
            sm.top_student()
        elif choice == "5":
            sm.unique_subjects()
        elif choice == "6":
            sm.grade_a_students()
        elif choice == "7":
            sm.export_to_csv()
        elif choice == "8":
            print("Exiting program. 👋")
            break
        else:
            print("[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()

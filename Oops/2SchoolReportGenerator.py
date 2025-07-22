# Base class
class Person:
    def __init__(self, name, id):
        self.name = name
        self._id = id  # private-like attribute

    def __str__(self):
        return f"{self.name} (ID: {self._id})"

# Subject class
class Subject:
    def __init__(self, name):
        self.name = name

# Student class
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)  # using super()
        self.__marks = {}  # encapsulated: subject name -> marks

    def add_mark(self, subject, mark):
        self.__marks[subject.name] = mark

    def get_marks(self):
        return self.__marks.copy()

    def __str__(self):
        return f"Student: {super().__str__()}"

# Teacher class
class Teacher(Person):
    def __init__(self, name, teacher_id):
        super().__init__(name, teacher_id)

    def update_mark(self, student, subject, mark):
        student.add_mark(subject, mark)

    def __str__(self):
        return f"Teacher: {super().__str__()}"

# ReportCard class
class ReportCard:
    def __init__(self, student):
        self.student = student

    def generate_report(self):
        print(f"\nReport Card for {self.student.name}")
        print("-" * 30)
        marks = self.student.get_marks()
        if not marks:
            print("No subjects recorded.")
        else:
            for subject, mark in marks.items():
                grade = self.grade_system(mark)
                print(f"{subject:<15}: {mark}/100 -> Grade: {grade}")
        print("-" * 30)

    def grade_system(self, mark):
        if mark >= 90:
            return 'A+'
        elif mark >= 75:
            return 'A'
        elif mark >= 60:
            return 'B'
        elif mark >= 40:
            return 'C'
        else:
            return 'F'

# Create subjects
math = Subject("Mathematics")
sci = Subject("Science")

# Create student and teacher
s1 = Student("Nila", "S1001")
t1 = Teacher("Mr. Ravi", "T501")

# Teacher assigns marks
t1.update_mark(s1, math, 85)
t1.update_mark(s1, sci, 92)

# Generate report card
report = ReportCard(s1)
report.generate_report()

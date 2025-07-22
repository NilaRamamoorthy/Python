# Online Course Portal

class Course:
    def __init__(self, title, code):
        self.title = title
        self.code = code
        self.students = []
        self.instructor = None

    def enroll_student(self, student):
        self.students.append(student)

    def assign_instructor(self, instructor):
        self.instructor = instructor

    def show_details(self):
        print(f"\n📚 Course: {self.title} ({self.code})")
        print(f"Instructor: {self.instructor.name if self.instructor else 'None'}")
        print("Students Enrolled:")
        for student in self.students:
            print("  🔹", student.name)


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Student(Person):
    def submit(self, assignment):
        print(f"📝 {self.name} submitted assignment: {assignment.title}")


class Instructor(Person):
    def assign(self, assignment, student):
        print(f"✅ {self.name} assigned '{assignment.title}' to {student.name}")


class Assignment:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class VideoAssignment(Assignment):
    def play(self):
        print(f"🎬 Playing video assignment: {self.title}")


class TextAssignment(Assignment):
    def read(self):
        print(f"📖 Reading text assignment: {self.title}")

# ----------------------
# 📌 Sample Usage
# ----------------------

if __name__ == "__main__":
    # Create Course
    course = Course("Python Programming", "CS101")

    # Create Instructor and Students
    inst = Instructor("Dr. Ravi", "ravi@edu.com")
    stu1 = Student("Meena", "meena@edu.com")
    stu2 = Student("Raj", "raj@edu.com")

    # Assign Instructor and Enroll Students
    course.assign_instructor(inst)
    course.enroll_student(stu1)
    course.enroll_student(stu2)

    # Create Assignments
    a1 = TextAssignment("Loops Assignment", "Solve 5 problems on loops.")
    a2 = VideoAssignment("Recursion Demo", "Watch the recursive call video.")

    # Assign & Submit Assignments
    inst.assign(a1, stu1)
    stu1.submit(a1)

    inst.assign(a2, stu2)
    stu2.submit(a2)

    # Play and Read
    a1.read()
    a2.play()

    # Show Course Info
    course.show_details()

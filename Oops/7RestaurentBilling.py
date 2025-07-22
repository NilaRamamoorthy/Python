class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name} ({self.gender}, {self.age} yrs)"


class Student(Person):
    total_students = 0  # class variable

    def __init__(self, name, age, gender, roll_no, course, email):
        super().__init__(name, age, gender)
        self.roll_no = roll_no
        self.course = course
        self.__email = email  # encapsulated
        Student.total_students += 1

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if Student.validate_email(email):
            self.__email = email
        else:
            print("Invalid email!")

    @classmethod
    def get_total_enrolled(cls):
        return cls.total_students

    @staticmethod
    def validate_email(email):
        return "@" in email and email.endswith(".com")

    def __str__(self):
        return (f"{super().__str__()} | Roll No: {self.roll_no} | "
                f"Course: {self.course} | Email: {self.__email}")


class EnrollmentSystem:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)
        print(f"Enrolled: {student.name}")

    def list_students(self):
        print("\n--- Enrolled Students ---")
        for s in self.students:
            print(s)

    def find_by_roll(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                return s
        return None
if __name__ == "__main__":
    system = EnrollmentSystem()

    s1 = Student("Nila", 20, "F", "S101", "Python", "nila@example.com")
    s2 = Student("Ravi", 21, "M", "S102", "Java", "ravi@code.com")

    system.enroll(s1)
    system.enroll(s2)

    system.list_students()

    print("\nTotal Enrolled:", Student.get_total_enrolled())

    print("\nFinding Student S102:")
    found = system.find_by_roll("S102")
    if found:
        print(found)
    else:
        print("Not found")

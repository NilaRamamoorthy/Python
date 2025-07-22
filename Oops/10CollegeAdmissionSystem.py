# College Admission System

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Department:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats

    def allocate_seat(self):
        if self.seats > 0:
            self.seats -= 1
            return True
        return False

    def __str__(self):
        return f"Department: {self.name}, Seats left: {self.seats}"

class AdmissionForm:
    def __init__(self, student_name, grade, documents_verified):
        self.__student_name = student_name  # Encapsulation
        self.__grade = grade
        self.__documents_verified = documents_verified

    def is_eligible(self):
        return self.__grade >= 60 and self.__documents_verified

class Student(Person):
    def __init__(self, name, age, grade, documents_verified):
        super().__init__(name, age)
        self.grade = grade
        self.documents_verified = documents_verified
        self.department = None

    def apply(self, department):
        form = AdmissionForm(self.name, self.grade, self.documents_verified)
        if form.is_eligible():
            if department.allocate_seat():
                self.department = department
                print(f"{self.name} admitted to {department.name}")
            else:
                print(f"No seats available in {department.name}")
        else:
            print(f"{self.name} is not eligible for admission")

    def __str__(self):
        dept = self.department.name if self.department else "Not assigned"
        return f"Student: {self.name}, Age: {self.age}, Department: {dept}"

# Sample usage
if __name__ == "__main__":
    d1 = Department("Computer Science", 2)
    d2 = Department("Mechanical", 1)

    s1 = Student("Anjali", 18, 85, True)
    s2 = Student("Ravi", 19, 58, True)
    s3 = Student("Meena", 18, 75, False)
    s4 = Student("John", 20, 90, True)

    s1.apply(d1)
    s2.apply(d1)
    s3.apply(d2)
    s4.apply(d1)

    print()
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print()
    print(d1)
    print(d2)

# Section 7: Composition & Aggregation Tasks (41–45)

# 41. Create a Car class that contains an Engine object (composition).
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started.")

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)  # Composition

    def start_car(self):
        print(f"{self.brand} car is starting...")
        self.engine.start()

c = Car("Toyota", 150)
c.start_car()

# 42. Design a Library class that has a list of Book objects (aggregation).
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books):
        self.books = books  # Aggregation

    def list_books(self):
        for book in self.books:
            print("Book:", book.title)

b1 = Book("Python Basics")
b2 = Book("Data Structures")
lib = Library([b1, b2])
lib.list_books()

# 43. Create a University class containing multiple Department objects (composition).
class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []  # Composition

    def add_department(self, dept_name):
        self.departments.append(Department(dept_name))

    def show_departments(self):
        print(f"{self.name} has the following departments:")
        for dept in self.departments:
            print("-", dept.name)

u = University("Tech University")
u.add_department("Computer Science")
u.add_department("Physics")
u.show_departments()

# 44. Build a Company object that aggregates many Employee instances.
class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees  # Aggregation

    def list_employees(self):
        print(f"{self.name} Employees:")
        for emp in self.employees:
            print("-", emp.name)

e1 = Employee("Amit")
e2 = Employee("Sara")
company = Company("TechCorp", [e1, e2])
company.list_employees()

# 45. Create a Flight object that includes Pilot, CabinCrew, and Passenger classes.
class Pilot:
    def __init__(self, name):
        self.name = name

class CabinCrew:
    def __init__(self, name):
        self.name = name

class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, pilot, crew_list, passenger_list):
        self.pilot = pilot                  # Composition
        self.crew = crew_list              # Aggregation
        self.passengers = passenger_list   # Aggregation

    def flight_info(self):
        print("Pilot:", self.pilot.name)
        print("Crew Members:")
        for crew in self.crew:
            print("-", crew.name)
        print("Passengers:")
        for p in self.passengers:
            print("-", p.name)

pilot = Pilot("Captain Raj")
crew = [CabinCrew("John"), CabinCrew("Lisa")]
passengers = [Passenger("Tom"), Passenger("Jerry")]

flight = Flight(pilot, crew, passengers)
flight.flight_info()

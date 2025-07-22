# Section 2: Inheritance Tasks (11–20)

# 11. Create a Vehicle class and inherit it in Car, Bike, and Truck classes.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass

c = Car("Toyota")
print("Car brand:", c.brand)

# 12. Use super() to call the parent class constructor from a child class.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        print(f"Car model: {self.model}")

c = Car("Honda", "Civic")

# 13. Create a Shape class and derive Square and Triangle. Override an area() method.
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

s = Square(4)
t = Triangle(5, 6)
print("Square Area:", s.area())
print("Triangle Area:", t.area())

# 14. Implement Multi-level Inheritance with Person → Employee → Manager.
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)
        self.dept = dept

m = Manager("Alice", 101, "HR")
print(m.name, m.emp_id, m.dept)

# 15. Demonstrate Multiple Inheritance with Father and Mother inherited by Child.
class Father:
    def skills(self):
        print("Father: Gardening, Carpentry")

class Mother:
    def skills(self):
        print("Mother: Painting, Cooking")

class Child(Father, Mother):
    def skills(self):
        super().skills()
        Mother.skills(self)
        print("Child: Coding")

c = Child()
c.skills()

# 16. Create a Teacher class and use hierarchical inheritance for MathTeacher, ScienceTeacher.
class Teacher:
    def teach(self):
        print("Teaching subject...")

class MathTeacher(Teacher):
    def teach_math(self):
        print("Teaching Math")

class ScienceTeacher(Teacher):
    def teach_science(self):
        print("Teaching Science")

m = MathTeacher()
s = ScienceTeacher()
m.teach()
m.teach_math()
s.teach()
s.teach_science()

# 17. Use isinstance() to check if an object belongs to a certain class.
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True

# 18. Use issubclass() to verify if a class is derived from another class.
class A:
    pass

class B(A):
    pass

print(issubclass(B, A))  # True
print(issubclass(A, B))  # False

# 19. Create a class hierarchy for an e-commerce platform (Product → ElectronicProduct → MobilePhone).
class Product:
    def __init__(self, name):
        self.name = name

class ElectronicProduct(Product):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

class MobilePhone(ElectronicProduct):
    def __init__(self, name, brand, price):
        super().__init__(name, brand)
        self.price = price

m = MobilePhone("Smartphone", "Samsung", 29999)
print(m.name, m.brand, m.price)

# 20. Demonstrate method resolution order (MRO) in a multiple inheritance example.
class A:
    def who(self):
        print("Class A")

class B(A):
    def who(self):
        print("Class B")

class C(A):
    def who(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.who()
print(D.__mro__)  # MRO: D → B → C → A → object

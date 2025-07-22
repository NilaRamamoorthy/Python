# Section 1: Classes and Objects (1–10)


# Create a Car class with attributes: brand, model, and price. Instantiate two cars and print details.

class Car:

   def __init__(self,brand,model,price):
      self.brand=brand
      self.model=model
      self.price=price
  
   def car_details(self):
      print(f"Car: {self.brand}, Model: {self.model}, Price: {self.price}")

car1=Car("Toyato","Camry",1800000)
car2=Car("Honda", "Civic",1600000)

car1.car_details()
car2.car_details()

# Create a BankAccount class with methods for deposit, withdraw, and balance check.

class BankAccount:
   def __init__(self,balance):
      self.balance=balance
    #   self.amount=amount
   def deposit(self,amount):
      self.balance+=amount
   def withdraw(self,amount):
      if self.balance>=amount:
         self.balance-=amount
      else:
            print("Insufficient balance.")
   def check_balance(self):
      print(f"Available Balance: {self.balance}")

update=BankAccount(10000)

update.deposit(20000)
update.withdraw(10000)
update.check_balance()
      
         
# Create a Student class with instance variables name, age, and grade. Accept data through the constructor.

class Student:
   def __init__(self,name,age,grade):
      self.name=name
      self.age=age
      self.grade=grade
   def display(self):
      print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student1=Student("Kamali",14,"B")

student1.display()


      
# Create a Circle class with method to calculate area and circumference.
import math
class Circle:
   def __init__(self,radius):
      self.radius=radius
   def area(self):
      print(f"Area of the circle is: {math.pi*(self.radius)**2}")
   def circumference(self):
      print(f"Circumference of the circle is: {2*math.pi*self.radius}")
area=Circle(23)
area.area()
area.circumference()
      
   
# Create a Book class with display_info() method and access data via object.

class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Price: ₹{self.price}")

book1 = Book("The Alchemist", "Paulo Coelho", 1988, 399)

book1.display_info()


# Create a Laptop class with class variable warranty_period shared among all objects.

class Laptop:
    warranty_period = 2  # years - class variable shared by all instances

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Usage
l1 = Laptop("Dell", "XPS 13")
l2 = Laptop("HP", "Pavilion")

print(f"{l1.brand} Warranty: {l1.warranty_period} years")
print(f"{l2.brand} Warranty: {l2.warranty_period} years")

# Create a Movie class where each instance tracks the total number of movies using a class variable.

class Movie:
    total_movies = 0  # class variable

    def __init__(self, title):
        self.title = title
        Movie.total_movies += 1  # increment on each new object

# Usage
m1 = Movie("Inception")
m2 = Movie("Interstellar")
m3 = Movie("Dune")

print("Total movies created:", Movie.total_movies)

# Create a Product class and demonstrate how instance variables differ from class variables.

class Product:
    category = "Electronics"  # class variable

    def __init__(self, name, price):
        self.name = name        # instance variable
        self.price = price      # instance variable

# Usage
p1 = Product("Phone", 50000)
p2 = Product("Laptop", 75000)

print(f"{p1.name} - ₹{p1.price} ({p1.category})")
print(f"{p2.name} - ₹{p2.price} ({p2.category})")

# Implement __str__ in a class Employee to display employee data in readable format.

class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, Role: {self.role}, Salary: ₹{self.salary}"

# Usage
e1 = Employee("Amit", "Manager", 90000)
print(e1)


# Write a program to compare two Rectangle objects using __eq__ method.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __eq__(self, other):
        return self.area() == other.area()

# Usage
r1 = Rectangle(10, 5)
r2 = Rectangle(25, 2)

print("Are rectangles equal?", r1 == r2)  # True if area is same








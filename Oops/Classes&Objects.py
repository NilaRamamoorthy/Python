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
   def check_balance(self):
      print(f"Available Balance: {self.balance}")

update=BankAccount(10000)

update.deposit(20000)

      
      
      
   
      
# Create a Student class with instance variables name, age, and grade. Accept data through the constructor.
# Create a Circle class with method to calculate area and circumference.
# Create a Book class with display_info() method and access data via object.
# Create a Laptop class with class variable warranty_period shared among all objects.
# Create a Movie class where each instance tracks the total number of movies using a class variable.
# Create a Product class and demonstrate how instance variables differ from class variables.
# Implement __str__ in a class Employee to display employee data in readable format.
# Write a program to compare two Rectangle objects using __eq__ method.







# Section 8: Real-World Applications (46–50)

# 46. Banking System with customer, account, transaction classes using full OOP concepts
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

class Account:
    def __init__(self, customer, balance=0):
        self.customer = customer
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

class Transaction:
    def __init__(self, account):
        self.account = account

    def perform_transaction(self, action, amount):
        if action == "deposit":
            self.account.deposit(amount)
        elif action == "withdraw":
            self.account.withdraw(amount)

cust = Customer("John", 101)
acct = Account(cust, 1000)
txn = Transaction(acct)
txn.perform_transaction("deposit", 500)
txn.perform_transaction("withdraw", 200)
print("Final Balance:", acct.get_balance())

# 47. Quiz Application using OOP (Question, Option, Quiz classes)
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for q in self.questions:
            ans = input(q.prompt)
            if ans.lower() == q.answer.lower():
                self.score += 1
        print("Your score:", self.score)

question_list = [
    Question("Capital of France?\na) Paris\nb) London\n", "a"),
    Question("2 + 2 = ?\na) 3\nb) 4\n", "b")
]

# Uncomment to run the interactive quiz
# q = Quiz(question_list)
# q.run()

# 48. Hotel Management System (Room, Booking, Customer classes using inheritance)
class Room:
    def __init__(self, room_no, room_type):
        self.room_no = room_no
        self.room_type = room_type
        self.is_booked = False

class CustomerBooking(Room):
    def __init__(self, room_no, room_type, customer_name):
        super().__init__(room_no, room_type)
        self.customer_name = customer_name

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Room {self.room_no} booked by {self.customer_name}")
        else:
            print("Room already booked.")

booking1 = CustomerBooking(101, "Deluxe", "Alice")
booking1.book()

# 49. School Management System using abstraction and polymorphism
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_role(self):
        pass

class Teacher(Person):
    def show_role(self):
        return f"{self.name} is a Teacher"

class Student(Person):
    def show_role(self):
        return f"{self.name} is a Student"

class Course:
    def __init__(self, title):
        self.title = title

class Grade:
    def __init__(self, student, grade):
        self.student = student
        self.grade = grade

t = Teacher("Mr. Rao")
s = Student("Nina")
print(t.show_role())
print(s.show_role())

# 50. Library System: borrowing, returning, searching, adding books
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"{title} has been borrowed.")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"{title} has been returned.")
                return
        print("Book not found or already returned.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                status = "Available" if book.available else "Not Available"
                print(f"{title} by {book.author} - {status}")
                return
        print("Book not found.")

lib = Library()
b1 = Book("1984", "George Orwell")
b2 = Book("The Alchemist", "Paulo Coelho")
lib.add_book(b1)
lib.add_book(b2)
lib.search_book("1984")
lib.borrow_book("1984")
lib.search_book("1984")
lib.return_book("1984")

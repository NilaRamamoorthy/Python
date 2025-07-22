# Section 3: Encapsulation Tasks (21–25)

# 21. Create a Student class with private attributes _name and _marks. Use getter/setter methods.
class Student:
    def __init__(self, name, marks):
        self._name = name          # private (by convention)
        self._marks = marks        # private (by convention)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Invalid marks")

s = Student("Nila", 85)
print("Student Name:", s.get_name())
s.set_marks(95)
print("Updated Marks:", s.get_marks())

# 22. Create a BankAccount class with balance as private variable. Ensure secure access via methods.
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # truly private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount(10000)
account.deposit(5000)
account.withdraw(3000)
print("Current Balance:", account.get_balance())

# 23. Build a UserProfile class with encapsulated email, phone and provide validation in setters.
class UserProfile:
    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    def set_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Invalid email")

    def get_email(self):
        return self.__email

    def set_phone(self, phone):
        if len(phone) == 10 and phone.isdigit():
            self.__phone = phone
        else:
            print("Invalid phone number")

    def get_phone(self):
        return self.__phone

user = UserProfile("user@example.com", "9876543210")
user.set_email("updated@example.com")
user.set_phone("1234567890")
print("Email:", user.get_email())
print("Phone:", user.get_phone())

# 24. Restrict direct access to salary field in a class Employee, use getters/setters.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary")

    def get_salary(self):
        return self.__salary

e = Employee("Ravi", 45000)
e.set_salary(50000)
print(f"{e.name}'s Salary:", e.get_salary())

# 25. Create a Locker system where the PIN is private and can only be changed via method.
class Locker:
    def __init__(self, pin):
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN!")

locker = Locker("1234")
locker.change_pin("1234", "5678")  # correct old pin
locker.change_pin("0000", "9999")  # incorrect old pin

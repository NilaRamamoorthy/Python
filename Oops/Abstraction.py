# Section 4: Abstraction Tasks (26–30)

from abc import ABC, abstractmethod

# 26. Use abc module to define an abstract class Payment with abstract method pay().
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using credit card.")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

p1 = CreditCardPayment()
p1.pay(5000)

p2 = UPI()
p2.pay(1500)

# 27. Create an abstract class Shape with abstract method area() and concrete method describe().
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a geometric shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
c.describe()
print("Circle Area:", c.area())

# 28. Implement Animal abstract class with abstract speak() method. Create subclasses Dog, Cat.
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

a1 = Dog()
a2 = Cat()
a1.speak()
a2.speak()

# 29. Create a template for Transport with abstract methods like start_engine() and stop_engine().
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Transport):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

t = Car()
t.start_engine()
t.stop_engine()

# 30. Create a base class Appliance with abstract method power_consumption(). Subclasses: Fridge, WashingMachine.
class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

class Fridge(Appliance):
    def power_consumption(self):
        return "Fridge consumes 150W"

class WashingMachine(Appliance):
    def power_consumption(self):
        return "Washing Machine consumes 500W"

f = Fridge()
w = WashingMachine()
print(f.power_consumption())
print(w.power_consumption())

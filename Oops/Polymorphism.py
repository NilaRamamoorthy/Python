# Section 5: Polymorphism Tasks (31–35)

# 31. Demonstrate method overriding with Animal base class and Dog subclass implementing speak().
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
d = Dog()
a.speak()
d.speak()

# 32. Use polymorphism via duck typing – write a function that calls draw() on different shape objects.
class Circle:
    def draw(self):
        print("Drawing a circle")

class Square:
    def draw(self):
        print("Drawing a square")

def render(shape):
    shape.draw()

c = Circle()
s = Square()
render(c)
render(s)

# 33. Simulate method overloading using default arguments in a class Calculator.
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print("Add 2 numbers:", calc.add(5, 10))
print("Add 3 numbers:", calc.add(5, 10, 15))
print("Add 0 numbers:", calc.add())

# 34. Simulate overloading using *args in a class Sum that can add 2, 3 or n numbers.
class Sum:
    def total(self, *args):
        return sum(args)

s = Sum()
print("Sum of 2 numbers:", s.total(10, 20))
print("Sum of 3 numbers:", s.total(1, 2, 3))
print("Sum of many numbers:", s.total(4, 5, 6, 7, 8))

# 35. Create a class Notification with method send(msg). Use subclasses SMS, Email, PushNotification.
class Notification:
    def send(self, msg):
        print("Sending notification:", msg)

class SMS(Notification):
    def send(self, msg):
        print("Sending SMS:", msg)

class Email(Notification):
    def send(self, msg):
        print("Sending Email:", msg)

class PushNotification(Notification):
    def send(self, msg):
        print("Sending Push Notification:", msg)

n1 = SMS()
n2 = Email()
n3 = PushNotification()

n1.send("Hi from SMS")
n2.send("Hi from Email")
n3.send("Hi from Push")

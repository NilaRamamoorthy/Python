#Basic Function Definition and Calling (1–10)

# Task 1: Define a function greet() that prints "Welcome to Python!".
def greet():
    print("Welcome to Python!")
greet()
print("-"*40)

# Task 2: Write a function add(a, b) that returns the sum of two numbers.
def add(a,b):
    return a+b
result=add(11,18)
print(f"Addition result is: {result}")
print("-"*40)

# Task 3: Define a function is_even(num) that returns True if the number is even.
def is_even(num):
    if num%2==0:
        return True
result=is_even(32)
print(f"The number is even: {result}")
print("-"*40)

# Task 4: Create a function cube(n) that returns the cube of a number.
def cube(n):
    return n**3
result=cube(3)
print(f"Cube of the number is : {result}")
print("-"*40)

# Task 5: Write a function hello(name) that prints "Hello, <name>".
def hello(name):
    print(f"Hello, {name}")
name=input("Enter your name: ")
hello(name)
print("-"*40)

# Task 6: Define a function with no code yet using pass.
def function():
    pass
function()
print("-"*40)

# Task 7: Create a function that takes two numbers and prints which is greater using if.
def compare(num1,num2):
    if num1>num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")
compare(20,23)
print("-"*40)
    
# Task 8: Write a function square_area(side) to return the area of a square.
def square_area(side):
    return side*2
result=square_area(20)
print(f"Area of the square is: {result}")
print("-"*40)

# Task 9: Create a menu-based function with options (view, add, exit) using if-else.
numbers=[1,2,3,4,5]
def options(option):
    if option=="1":
        print(numbers)
    if option=="2":
        add=int(input("Enter number to add: "))
        numbers.append(add)
        print(numbers)
    if option=="3":
        print("You are about to exit")
print("----Menu----")
print("1.View")
print("2.Add")
print("3.Exit")
option=input("Choose an option(1,2,3): ")
options(option)

# Task 10: Call a function multiple times in a loop to show reusability.
def greet():
    print("Welcome User!")
num=1
while num<6:
    greet()
    num+=1
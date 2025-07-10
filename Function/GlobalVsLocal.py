# Global vs Local Variables (16–20)
# Task 16: Create a global variable x = 100, and print it inside a function.
x=100
def function():
    print(x)
function()
print("-"*40)

# Task 17: Create a function with a local variable and show that it's not accessible outside.
def local():
    y=200
print(y) #raises error of undefined variable
print("-"*40)

# Task 18: Use both a global and a local variable in the same function and print both.
num1=200
def variables():
    num2=400
    print(f"Global variable: {num1} ,Local variable: {num2}")
variables()
print("-"*40)

# Task 19: Modify a global variable inside a function using the global keyword.
def change():
     global num3
     num3=400
change()
print(f"Value with global keyword: {num3}")
print("-"*40)

# Task 20: Show that a variable with the same name inside a function doesn’t affect the global one.
num4=4
def variable_with_same_name():
    num4=8

variable_with_same_name()
print(f"Global and local variable with same name: {num4}") #Takes the value of the local variable
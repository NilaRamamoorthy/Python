# Task 41: Assign a function to a variable and call it using the new name
def greet():
    return "Hello from greet!"

new_greet = greet
print(new_greet())
print("-"*40)

# Task 42: Function that takes another function as argument
def shout(text):
    return text.upper()

def call_func(func):
    result = func("hello world")
    return result

print(call_func(shout))
print("-"*40)

# Task 43: Function that returns another function
def outer():
    def inner():
        return "This is the inner function!"
    return inner

returned_func = outer()
print(returned_func())
print("-"*40)

# Task 44: Pass a lambda function as an argument
def apply_function(f, x):
    return f(x)

print(apply_function(lambda x: x * 3, 10))  # 10 * 3 = 30
print("-"*40)

# Task 45: Take two numbers and a function, apply it
def calculate(a, b, operation):
    return operation(a, b)

add = lambda x, y: x + y
subtract = lambda x, y: x - y

print("Add:", calculate(5, 3, add))        # 5 + 3 = 8
print("Subtract:", calculate(5, 3, subtract))  # 5 - 3 = 2
print("-"*40)
# Task 46: Function with nested function that prints a message
def outer_message():
    def inner():
        print("Hello from the inner function!")
    inner()
outer_message()
print("-"*40)

# Task 47: Function using inner function to double a number and return it
def double_number(n):
    def inner_double(x):
        return x * 2
    return inner_double(n)

result = double_number(10)
print("Doubled Result →", result)
print("-"*40)
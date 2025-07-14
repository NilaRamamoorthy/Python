# Define operation functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

# Calculator function that takes two numbers and an operation
def calculator(x, y, operation_func):
    return operation_func(x, y)

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

# Map operator symbol to function
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Check if operation is valid
if op in operations:
    result = calculator(num1, num2, operations[op])
    print(f"Result: {result}")
else:
    print("Invalid operation selected.")

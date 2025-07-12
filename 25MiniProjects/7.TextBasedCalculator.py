# Text-Based Calculator

history = []

# Calculator operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else " Cannot divide by zero"

# Function to perform calculation
def calculate(op, num1, num2):
    if op == "add":
        return add(num1, num2)
    elif op == "subtract":
        return subtract(num1, num2)
    elif op == "multiply":
        return multiply(num1, num2)
    elif op == "divide":
        return divide(num1, num2)
    else:
        return " Invalid operation"

# Main menu loop
def calculator():
    print("Welcome to Text-Based Calculator")
    while True:
        print("\n--- CALCULATOR MENU ---")
        print("Operations: add, subtract, multiply, divide")
        print("Type 'history' to view past results or 'exit' to quit")

        operation = input("Enter operation: ").lower()
        
        if operation == "exit":
            print(" Exiting Calculator.")
            break
        elif operation == "history":
            print("\nCalculation History:")
            if not history:
                print("No calculations yet.")
            for entry in history:
                print(entry)
            continue

        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            result = calculate(operation, n1, n2)
            if isinstance(result, str):
                print(result)
            else:
                print(f" Result: {result}")
                history.append(f"{operation}({n1}, {n2}) = {result}")
        except ValueError:
            print(" Invalid input. Please enter numbers.")

# Run the calculator
calculator()

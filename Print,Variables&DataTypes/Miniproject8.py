# Simple Calculator

# Step 1: Prompt the user for two numbers and an operation
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose operation (add, subtract, multiply, divide): ")

# Step 2: Show types of inputs before conversion
print(f"\nBefore conversion:")
print(f"num1: {num1} (Type: {type(num1)})")
print(f"num2: {num2} (Type: {type(num2)})")
print(f"operation: {operation} (Type: {type(operation)})")

# Step 3: Convert inputs to float for calculation
num1 = float(num1)
num2 = float(num2)

# Step 4: Perform the chosen operation
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

# Step 5: Print the result and its type
print(f"\nResult: {result}")
print(f"Type of result: {type(result)}" )

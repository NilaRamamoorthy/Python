# Simple Calculator App
# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Input operation
operation = input("Choose operation (+, -, *, /, %, **): ").strip()

# Perform calculation using if-elif-else
if operation == '+':
    result = num1 + num2
    op_name = "Addition"
elif operation == '-':
    result = num1 - num2
    op_name = "Subtraction"
elif operation == '*':
    result = num1 * num2
    op_name = "Multiplication"
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        op_name = "Division"
    else:
        result = "Error (division by zero)"
        op_name = "Division"
elif operation == '%':
    if num2 != 0:
        result = num1 % num2
        op_name = "Modulus"
    else:
        result = "Error (modulus by zero)"
        op_name = "Modulus"
elif operation == '**':
    result = num1 ** num2
    op_name = "Exponentiation"
else:
    result = "Invalid operation"
    op_name = "Unknown"

# Output using formatted string
print("\n--- Result ---")
print(f"Operation : {op_name}")
print(f"Input     : {num1} {operation} {num2}")
print(f"Result    : {result}")
print("------------------------")

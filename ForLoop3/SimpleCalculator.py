# 13. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
if op == '+':
    print(f"Result: {num1 + num2}")
elif op == '-':
    print(f"Result: {num1 - num2}")
elif op == '*':
    print(f"Result: {num1 * num2}")
elif op == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
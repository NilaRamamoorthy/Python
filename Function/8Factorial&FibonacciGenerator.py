# Recursive Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive Fibonacci Function
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example Usage
num1 = 5
num2 = 7

print(f"Factorial of {num1} is: {factorial(num1)}")
print(f"{num2}th Fibonacci number is: {fibonacci(num2)}")

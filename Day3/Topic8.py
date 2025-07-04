# Conditional Statements – Basic (41–50)

# Task 41
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
print("-" * 40)

# Task 42
age = int(input("Enter your age: "))
if age < 18:
    print("You are a Minor.")
else:
    print("You are an Adult.")
print("-" * 40)

# Task 43
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Fail")
print("-" * 40)

# Task 44
temp = float(input("Enter the temperature in °C: "))
if temp > 35:
    print("Hot")
elif 25 <= temp <= 35:
    print("Warm")
else:
    print("Cool")
print("-" * 40)

# Task 45
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
print("-" * 40)

# Task 46
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials.")
print("-" * 40)

# Task 47
is_raining = input("Is it raining? (yes/no): ").lower()
if is_raining == "yes":
    has_umbrella = input("Do you have an umbrella? (yes/no): ").lower()
    if has_umbrella == "yes":
        print("You can go outside.")
    else:
        print("Better stay indoors.")
else:
    print("Enjoy your day!")
print("-" * 40)

# Task 48
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").lower()
if age >= 18 and nationality == "indian":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print("-" * 40)

# Task 49
operation = input("Choose operation (add/sub): ").lower()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "add":
    print("Result:", num1 + num2)
elif operation == "sub":
    print("Result:", num1 - num2)
else:
    print("Invalid operation.")
print("-" * 40)

# Task 50
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 40 and attendance >= 75:
    print("Passed")
else:
    print("Failed")
print("-" * 40)

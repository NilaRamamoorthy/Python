# Basic Exception Handling (1–10)

# 1. Divide two numbers, handle ZeroDivisionError and ValueError
try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")

# 2. Take user input for age, raise error if input is non-numeric or negative
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is", age)
except ValueError as e:
    print("Invalid input:", e)

# 3. Open a file, handle FileNotFoundError
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")

# 4. Read from a closed file, handle ValueError
try:
    file = open("sample.txt", "w")
    file.close()
    file.read()
except ValueError:
    print("Error: Cannot read from a closed file.")

# 5. Handle IndexError when accessing list items by user input index
try:
    items = ["apple", "banana", "cherry"]
    index = int(input("Enter list index (0–2): "))
    print("Item:", items[index])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Invalid index input.")

# 6. Handle KeyError when accessing a dictionary with a missing key
try:
    data = {"name": "Alice", "age": 30}
    key = input("Enter dictionary key: ")
    print("Value:", data[key])
except KeyError:
    print("Error: Key not found in dictionary.")

# 7. Ask user to enter a number, convert to int, catch ValueError
try:
    num = int(input("Enter a number: "))
    print("Number entered:", num)
except ValueError:
    print("Error: That's not a valid integer.")

# 8. Catch TypeError when trying to add string and integer
try:
    result = "Age: " + 25
    print(result)
except TypeError:
    print("Error: Cannot concatenate string and integer.")

# 9. Catch AttributeError by calling a non-existent method on an object
try:
    name = "Alice"
    name.run()  # This method doesn't exist
except AttributeError:
    print("Error: 'str' object has no method 'run'.")

# 10. Handle NameError when accessing an undefined variable
try:
    print(score)  # 'score' is not defined
except NameError:
    print("Error: Variable 'score' is not defined.")


# Multiple Except, Else, Finally Blocks (11–20)

# 11. Demonstrate try with else: divide numbers only if no exception
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
except ValueError:
    print("Error: Invalid input. Please enter integers.")
else:
    print("Result:", a / b)

# 12. Demonstrate try with finally: print "Done" regardless of error
try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("Error: Invalid number.")
finally:
    print("Done")  # Always runs

# 13. Use multiple except blocks to catch ValueError and ZeroDivisionError
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    print("Division:", num1 / num2)
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# 14. Show that finally runs even when exception is raised and not caught
try:
    print(10 / 0)  # Raises ZeroDivisionError
finally:
    print("This will print even though exception is not caught.")

# 15. Demonstrate combining else and finally together
try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise ValueError("Number must be positive.")
except ValueError as e:
    print("Exception:", e)
else:
    print("Good, you entered:", num)
finally:
    print("Process finished.")

# 16. Handle exception in file reading and ensure file is closed using finally
try:
    file = open("nonexistent.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File does not exist.")
finally:
    try:
        file.close()
    except NameError:
        print("File was never opened.")
    else:
        print("File closed.")

# 17. Nested try-except blocks: one inside another
try:
    num1 = int(input("Outer try: Enter number: "))
    try:
        print("Inner try: Reciprocal =", 1 / num1)
    except ZeroDivisionError:
        print("Inner except: Cannot divide by zero.")
except ValueError:
    print("Outer except: Invalid input.")

# 18. Handle a situation where multiple types of exceptions might occur
try:
    nums = [10, 20, 30]
    index = int(input("Enter index: "))
    divisor = int(input("Enter divisor: "))
    print(nums[index] / divisor)
except IndexError:
    print("Error: Index out of range.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input.")

# 19. Use except Exception as a generic fallback and explain it
try:
    result = "text" + 5
except Exception as e:
    print("Generic Exception caught:", e)
# Explanation: This catches any kind of exception and stores it in 'e'. Useful when exact error type is unknown.

# 20. Demonstrate incorrect nesting of try-except-finally and correct it
# Incorrect:
# try:
#     print("Hello")
# except:
# finally:  # SyntaxError: finally without try
#     print("Incorrect nesting")

# Correct:
try:
    print("Correct nesting demo")
except Exception:
    print("Handled exception")
finally:
    print("Finally always runs")

# Raise Statement (21–30)

# 21. Raise ValueError manually if user enters a negative number
num = int(input("Enter a positive number: "))
if num < 0:
    raise ValueError("Negative numbers are not allowed.")
print("You entered:", num)

# 22. Raise TypeError if function argument is not a string
def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    print("Hello,", name)

greet("Alice")
# greet(123)  # Uncomment to test TypeError

# 23. Create a function that only accepts positive integers, use raise
def square(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    return n * n

print("Square:", square(5))

# 24. Simulate a login system and raise exception if password is incorrect
def login(username, password):
    correct_password = "secure123"
    if password != correct_password:
        raise PermissionError("Incorrect password.")
    print(f"Welcome, {username}!")

login("admin", "secure123")
# login("admin", "wrongpass")  # Uncomment to test

# 25. Raise an error if a required key is missing from a dictionary
data = {"name": "John", "age": 30}
if "email" not in data:
    raise KeyError("Missing required key: 'email'.")

# 26. Raise a ZeroDivisionError with custom error message
numerator = 10
denominator = 0
if denominator == 0:
    raise ZeroDivisionError("Cannot divide by zero (custom message).")
print(numerator / denominator)

# 27. Use assert to raise error if number is not even
number = int(input("Enter an even number: "))
assert number % 2 == 0, "The number is not even."
print("You entered an even number.")

# 28. Validate email format and raise a ValueError if invalid
import re

def validate_email(email):
    pattern = r'^\w+@\w+\.\w+$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email format.")
    print("Email is valid.")

validate_email("user@example.com")
# validate_email("invalidemail.com")  # Uncomment to test

# 29. Raise an exception if list is empty before processing
items = []
if not items:
    raise ValueError("Cannot process empty list.")
print("Processing list:", items)

# 30. Raise error if file is empty before reading
try:
    with open("example.txt", "r") as file:
        content = file.read()
        if not content.strip():
            raise EOFError("File is empty.")
        print(content)
except FileNotFoundError:
    print("File not found.")
    
# Custom/User-Defined Exceptions (31–40)

# 31. Create a custom exception NegativeNumberError and raise it
class NegativeNumberError(Exception):
    pass

num = int(input("Enter a number: "))
if num < 0:
    raise NegativeNumberError("Negative numbers are not allowed.")
print("You entered:", num)

# 32. Define InvalidAgeError and use it in age-based logic
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age <= 0 or age > 120:
        raise InvalidAgeError("Invalid age entered.")
    print("Valid age:", age)

check_age(25)
# check_age(-5)  # Uncomment to test

# 33. Build a banking app with InsufficientFundsError
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds.")
    print(f"Withdrawn: {amount}, Remaining balance: {balance - amount}")

withdraw(1000, 300)
# withdraw(500, 800)  # Uncomment to test

# 34. Create a grading app and raise GradeOutOfRangeError for marks > 100
class GradeOutOfRangeError(Exception):
    pass

def assign_grade(marks):
    if marks > 100:
        raise GradeOutOfRangeError("Marks cannot exceed 100.")
    print("Grade assigned for marks:", marks)

assign_grade(85)
# assign_grade(105)  # Uncomment to test

# 35. Raise UnauthorizedAccessError in a mock role-based system
class UnauthorizedAccessError(Exception):
    pass

def access_control(role):
    if role != "admin":
        raise UnauthorizedAccessError("Access denied for non-admin users.")
    print("Access granted.")

access_control("admin")
# access_control("guest")  # Uncomment to test

# 36. Use custom exception for invalid file format in a file uploader
class InvalidFileFormatError(Exception):
    pass

def upload_file(filename):
    if not filename.endswith(('.jpg', '.png', '.gif')):
        raise InvalidFileFormatError("Only image files are allowed.")
    print("File uploaded successfully:", filename)

upload_file("image.jpg")
# upload_file("document.pdf")  # Uncomment to test

# 37. Create LoginAttemptsExceeded for user login system
class LoginAttemptsExceeded(Exception):
    pass

def login_user(attempts):
    if attempts > 3:
        raise LoginAttemptsExceeded("Too many failed login attempts.")
    print("Login attempt:", attempts)

login_user(2)
# login_user(4)  # Uncomment to test

# 38. Create a class-level exception to enforce object state rules
class InvalidStateError(Exception):
    pass

class LightSwitch:
    def __init__(self):
        self.state = "off"

    def turn_off(self):
        if self.state == "off":
            raise InvalidStateError("Light is already off.")
        self.state = "off"
        print("Light turned off.")

    def turn_on(self):
        if self.state == "on":
            raise InvalidStateError("Light is already on.")
        self.state = "on"
        print("Light turned on.")

switch = LightSwitch()
switch.turn_on()
# switch.turn_on()  # Uncomment to test

# 39. Create a file validation system that raises FileTooLargeError
class FileTooLargeError(Exception):
    pass

def validate_file_size(size_kb):
    if size_kb > 1024:
        raise FileTooLargeError("File size exceeds 1MB limit.")
    print("File size accepted:", size_kb, "KB")

validate_file_size(500)
# validate_file_size(2048)  # Uncomment to test

# 40. Build a temperature converter and raise exception if below absolute zero
class TemperatureBelowAbsoluteZero(Exception):
    pass

def convert_to_kelvin(celsius):
    if celsius < -273.15:
        raise TemperatureBelowAbsoluteZero("Temperature below absolute zero.")
    return celsius + 273.15

print("Temperature in Kelvin:", convert_to_kelvin(0))
# print(convert_to_kelvin(-300))  # Uncomment to test


# Exception Handling in Loops and Functions (41–45)

# 41. Ask user to enter 5 valid integers using a loop, handle bad inputs
valid_numbers = []
while len(valid_numbers) < 5:
    try:
        num = int(input(f"Enter integer {len(valid_numbers)+1}/5: "))
        valid_numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
print("Collected integers:", valid_numbers)

# 42. Write a function that opens and reads file and handles any error
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied."
    except Exception as e:
        return f"Unexpected error: {e}"

print(read_file("sample.txt"))

# 43. Handle exception in recursive function (e.g., factorial)
def factorial(n):
    try:
        if n < 0:
            raise ValueError("Cannot compute factorial of negative number.")
        if n == 0:
            return 1
        return n * factorial(n - 1)
    except RecursionError:
        return "Error: Maximum recursion depth exceeded."

print("Factorial of 5:", factorial(5))
# print("Factorial of -1:", factorial(-1))  # Uncomment to test

# 44. Inside a loop, catch and skip bad inputs instead of crashing
inputs = ["10", "abc", "25", "3.14", "-5", "hello", "7"]
converted = []
for val in inputs:
    try:
        converted.append(int(val))
    except ValueError:
        print(f"Skipping invalid input: {val}")
print("Valid integers:", converted)

# 45. Demonstrate try-except inside a list comprehension (with filtering)
raw_data = ["5", "x", "12", "hello", "7"]
filtered_ints = [int(i) for i in raw_data if i.isdigit()]
print("Filtered ints from list comprehension:", filtered_ints)

# Real-Life Use Case Tasks (46–50)

# 46. Build a calculator that uses exception handling for all basic operations
def calculator(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        else:
            raise ValueError("Unsupported operation.")
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"

print("Result:", calculator(10, 0, '/'))

# 47. Build a file copy tool that handles all common file errors
def copy_file(src, dest):
    try:
        with open(src, "r") as f1, open(dest, "w") as f2:
            data = f1.read()
            f2.write(data)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print("Unexpected error:", e)

# copy_file("source.txt", "destination.txt")

# 48. Build a user registration form that validates all fields and raises exceptions
class InvalidInput(Exception):
    pass

def register_user(username, age, email):
    if not username.isalnum():
        raise InvalidInput("Username must be alphanumeric.")
    if not (0 < age < 120):
        raise InvalidInput("Age must be between 1 and 119.")
    if "@" not in email or "." not in email:
        raise InvalidInput("Invalid email address.")
    print("Registration successful!")

try:
    register_user("User123", 25, "user@example.com")
except InvalidInput as e:
    print("Registration error:", e)

# 49. Create an app that logs all exceptions to a file (using logging)
import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

def risky_operation():
    try:
        a = int("abc")
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        print("An error occurred. Check 'errors.log'.")

risky_operation()

# 50. Simulate a payment gateway that handles all input and system errors gracefully
def payment_gateway(card_number, amount):
    try:
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Invalid card number.")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        # Simulate payment
        print(f"Payment of ₹{amount} successful using card ending with {card_number[-4:]}.")
    except ValueError as e:
        print("Payment error:", e)
    except Exception as e:
        print("Unexpected system error:", e)

payment_gateway("1234567812345678", 1500)
# payment_gateway("1234abcd", -500)  # Uncomment to test


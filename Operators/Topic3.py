# Logical Operators Tasks (15–20)

# Task 15
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"

if age > 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")
print("-" * 40)

# Task 16
confirmation = input("Do you want to continue? (yes/y/no/n): ").lower()

if confirmation == "yes" or confirmation == "y":
    print("Confirmed.")
else:
    print("Not confirmed.")
print("-" * 40)

# Task 17
num = int(input("Enter a number: "))

if not num > 100:
    print("Number is not greater than 100.")
else:
    print("Number is greater than 100.")
print("-" * 40)

# Task 18
age = int(input("Enter your age: "))
dress_code = input("Enter your dress code (formal/casual): ").lower()

if age >= 21 and dress_code == "formal":
    print("Entry allowed to the club.")
else:
    print("Entry denied.")
print("-" * 40)

# Task 19
a = input("Enter first condition (true/false): ").lower() == "true"
b = input("Enter second condition (true/false): ").lower() == "true"

print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT a:", not a)
print("NOT b:", not b)
print("-" * 40)

# Task 20
maths = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))

if (maths >= 50 and science >= 50) or (maths + science >= 120):
    print("Result: Pass")
else:
    print("Result: Fail")
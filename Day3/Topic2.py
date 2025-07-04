# Comparison Operators Tasks (9–14)

# Task 9
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Equal:", num1 == num2)
print("Not equal:", num1 != num2)
print("Greater than:", num1 > num2)
print("Less than:", num1 < num2)
print("Greater than or equal to:", num1 >= num2)
print("Less than or equal to:", num1 <= num2)
print("-" * 40)

# Task 10
age = int(input("Enter your age: "))

if age > 18:
    print("You are older than 18.")
else:
    print("You are not older than 18.")
print("-" * 40)

# Task 11
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Strings are equal:", str1 == str2)
print("Strings are not equal:", str1 != str2)
print("-" * 40)

# Task 12
score1 = int(input("Enter first exam score: "))
score2 = int(input("Enter second exam score: "))

if score1 > score2:
    print("First score is higher.")
elif score1 < score2:
    print("Second score is higher.")
else:
    print("Both scores are equal.")
print("-" * 40)

#Task 13
# Get input from the user
number = int(input("Enter a number: "))

# Define the range
lower_limit = 10
upper_limit = 100

# Check if the number is within the range
if number >= lower_limit and number <= upper_limit:
    print(f"The number {number} lies between {lower_limit} and {upper_limit}.")
else:
    print(f"The number {number} is outside the range {lower_limit} to {upper_limit}.")
#Task 14
# Get score input from the user
score = int(input("Enter your score: "))

# Check if the score is a passing mark
if score > 50:
    print("You have passed!")
else:
    print("You have not passed.")

# User Age Classification System

# Input
name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))

# Classify age using if-elif-else
if age < 13:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teenager"
elif 20 <= age <= 59:
    category = "Adult"
else:
    category = "Senior"

# Output result using formatted string
print("\n--- Age Classification ---")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"Category   : {category}")
print("----------------------------")

# Online Voting Eligibility Checker

# Input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship: ").strip().capitalize()

# Show data types
print("\n--- Data Types ---")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of citizenship: {type(citizenship)}")

# Check eligibility
print("\n--- Eligibility Result ---")
if age >= 18 and citizenship == "Indian":
    print(f"Hello {name}, you are eligible to vote in India.")
else:
    print(f"Sorry {name}, you are NOT eligible to vote in India.")

print(f"age >= 18: {age >= 18}")
print(f"citizenship == 'Indian': {citizenship == 'Indian'}")
print(f"Eligibility condition result: {age >= 18 and citizenship == 'Indian'}")

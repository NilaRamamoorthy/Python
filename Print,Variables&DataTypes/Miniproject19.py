import random

# Email Formatter with Symbol and Random Number

# Step 1: Ask for user's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Step 2: Choose a random symbol and random number
symbols = ['.', '_', '-']
symbol = random.choice(symbols)
random_number = random.randint(11, 999)

# Step 3: Generate email using f-string
email = f"{first_name.lower()}{symbol}{last_name.lower()}{random_number}@example.com"

# Step 4: Print the email and its type
print(f"\nGenerated Email: {email}")
print(f"Type of email: {type(email)}")

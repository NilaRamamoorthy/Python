# Voting Eligibility Checker

# Step 1: Ask for age
age = input("Enter your age: ")

# Step 2: Show type before conversion
print(f"\nBefore conversion: {age} (Type: {type(age)})")

# Step 3: Convert to integer
age = int(age)

# Step 4: Check eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Step 5: Show type after conversion
print(f"After conversion: {age} (Type: {type(age)})")

# Age and Income-Based Loan Checker
# Input
age = int(input("Enter your age: "))
income = float(input("Enter your monthly income (₹): "))

# Check eligibility using if-elif-else and logical operators
if age < 21:
    print("\n Not eligible for loan: You must be at least 21 years old.")
elif income < 20000:
    print("\n Not eligible for loan: Your income must be ₹20,000 or more.")
else:
    print("\n Congratulations! You are eligible to apply for a loan.")

# Display summary using formatted output
print("\n--- Applicant Summary ---")
print(f"Age     : {age} years")
print(f"Income  : ₹{income:,.2f}")
print("------------------------------")

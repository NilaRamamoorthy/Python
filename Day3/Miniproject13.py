# Salary Tax Deduction Calculator
# Input: base salary
salary = float(input("Enter your annual base salary (₹): "))

# Initialize tax
tax = 0

# Calculate tax using if-elif-else
if salary < 500000:
    tax = 0
elif salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.10

# Deduct tax using assignment operator
net_salary = salary
net_salary -= tax 

# Output
print("\n--- Salary Breakdown ---")
print(f"Base Salary   : ₹{salary:,.2f}")
print(f"Tax Deducted  : ₹{tax:,.2f}")
print(f"Net Salary    : ₹{net_salary:,.2f}")
print("-----------------------------")

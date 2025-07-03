# Electricity Bill Calculator

# Input
name = input("Enter customer name: ").strip().title()
units = int(input("Enter number of units consumed: "))

# Initialize bill amount
bill = 0

# Calculate based on units
if units <= 100:
    bill = units * 2
elif units <= 300:
    bill = units * 3
else:
    bill = units * 5

# Display the bill using f-string
print("\n--- Electricity Bill ---")
print(f"Customer Name : {name}")
print(f"Units Consumed: {units} units")
print(f"Total Bill    : ₹{bill}")
print("-------------------------")

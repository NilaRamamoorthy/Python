# Mobile Recharge Validator

# Input
mobile = input("Enter your mobile number: ").strip()
amount = float(input("Enter recharge amount (₹): "))

# Validation using len(), logical and comparison operators
if len(mobile) == 10 and mobile.isdigit():
    if amount > 10:
        print("\n Recharge successful!")
        print(f"Mobile: {mobile}")
        print(f"Amount: ₹{amount:.2f}")
    else:
        print("\n Recharge failed: Amount must be greater than ₹10.")
else:
    print("\n Recharge failed: Invalid mobile number (must be 10 digits).")

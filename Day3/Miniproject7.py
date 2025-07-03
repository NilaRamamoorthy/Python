# Product Discount System
# Input
product = input("Enter product name: ").strip().title()
price = float(input("Enter product price (₹): "))
discount_percent = float(input("Enter discount percentage (%): "))

# Calculate discount using arithmetic
discount_amount = price * discount_percent / 100

# Apply discount using assignment operator
price -= discount_amount  

# Output using f-string
print("\n--- Discount Summary ---")
print(f"Product         : {product}")
print(f"Discount Given  : ₹{discount_amount:.2f}")
print(f"Final Price     : ₹{price:.2f}")
print("---------------------------")

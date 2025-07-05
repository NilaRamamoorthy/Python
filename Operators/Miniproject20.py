# E-commerce Mini Checkout System
# Inputs
price = float(input("Enter product price (₹): "))
quantity = int(input("Enter quantity: "))
discount_code = input("Enter discount code (if any): ").strip().upper()

# Predefined discount codes
valid_discounts = {
    "SAVE10": 10,   
    "SAVE20": 20,   
    "FESTIVE": 15  
}

# Calculate subtotal
total = price * quantity

# Validate discount code using 'in'
if discount_code in valid_discounts:
    discount_percent = valid_discounts[discount_code]
    discount_amount = total * discount_percent / 100
    total -= discount_amount  # Assignment operator
    print(f"\n Discount '{discount_code}' applied: -₹{discount_amount:.2f}")
else:
    print("\n No valid discount applied.")

# Final bill
print("\n--- Final Bill ---")
print(f"Price per item  : ₹{price:.2f}")
print(f"Quantity        : {quantity}")
print(f"Total Payable   : ₹{total:.2f}")
print("---------------------------")

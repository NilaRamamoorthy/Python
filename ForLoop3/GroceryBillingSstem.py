 #3. Grocery Billing System
prices = {"milk": 40, "bread": 30, "rice": 70, "eggs": 60}
cart = input("Enter items (comma separated): ").split(',')
total = 0
for item in cart:
    item = item.strip()
    if item in prices:
        total += prices[item]
if total > 1000:
    total *= 0.9
print(f"Total bill: ₹{total:.2f}")
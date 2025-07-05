items = {"milk": 40, "bread": 30, "rice": 70, "eggs": 60}
cart = input("Enter items to buy (comma separated): ").split(",")
total = 0

for item in cart:
    item = item.strip()
    if item in items:
        total += items[item]

if total > 1000:
    total *= 0.9

print(f"Total bill after discount (if any): ₹{total:.2f}")
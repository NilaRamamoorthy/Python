prices = {"apple": 30, "banana": 10, "milk": 40, "bread": 25, "rice": 60}
items = input("Enter items bought (comma separated): ").split(',')
total = 0

for item in items:
    item = item.strip()
    if item in prices:
        total += prices[item]

if len(items) > 5:
    total -= 50

print(f"Total Price: ₹{total}")
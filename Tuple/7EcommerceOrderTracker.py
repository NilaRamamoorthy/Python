
# 7. E-commerce Order Tracker
orders = [
    (1001, 'Alice', ('Laptop', 'Mouse', 'Bag')),
    (1002, 'Bob', ('Phone', 'Charger', 'Case'))
]
for oid, cname, items in orders:
    print(f"Order {oid} by {cname}:")
    for item in items:
        print(" -", item)



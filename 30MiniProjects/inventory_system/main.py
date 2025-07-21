from stock_ops import *

# Add sample items
add_item("Pen", 50, 10.0, "Stationery", "OfficeMart")
add_item("Notebook", 5, 50.0, "Stationery", "NoteCo")
add_item("Chair", 2, 750.0, "Furniture", "FurniWorld")

print("Inventory:")
for item, details in inventory.items():
    print(f"{item}: Quantity={details[0]}, Price={details[1]}")

print("\nRestock Alert (threshold < 10):")
alerts = restock_alert()
for item in alerts:
    print(f"{item} - Only {alerts[item][0]} left!")

print("\nAll Categories:", categories)
print("All Suppliers:", suppliers)

# Update an item
update_stock("Notebook", quantity=15)

print("\nUpdated Inventory:")
print(inventory)

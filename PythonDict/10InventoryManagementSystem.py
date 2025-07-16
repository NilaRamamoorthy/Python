# Initial inventory
inventory = {
    "pen": {"stock": 50, "min_required": 20, "supplier": "ABC Stationery"},
    "notebook": {"stock": 10, "min_required": 15, "supplier": "XYZ Paper"},
    "eraser": {"stock": 5, "min_required": 10, "supplier": "ABC Stationery"}
}

# 1. Alert for low-stock items
print("Low Stock Alerts:")
for item, info in inventory.items():
    if info["stock"] < info["min_required"]:
        print(f"{item} - Stock: {info['stock']}, Min Required: {info['min_required']}")

# 2. Add new item using setdefault()
inventory.setdefault("marker", {"stock": 25, "min_required": 10, "supplier": "Marker Co."})

# 3. Delete discontinued items
discontinued = "eraser"
inventory.pop(discontinued, None)

# 4. Export low-stock items using dictionary comprehension
low_stock_items = {
    item: info for item, info in inventory.items()
    if info["stock"] < info["min_required"]
}

print("\nExported Low-Stock Items:")
for item, data in low_stock_items.items():
    print(f"{item}: Stock = {data['stock']}, Required = {data['min_required']}")

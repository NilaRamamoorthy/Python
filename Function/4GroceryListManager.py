# Grocery List Manager

inventory = {}

def add_items(**kwargs):
    global inventory
    for item, quantity in kwargs.items():
        inventory[item] = inventory.get(item, 0) + quantity
    print("Items added to inventory.")

def total_items():
    return sum(inventory.values())

def sorted_inventory():
    return sorted(inventory.items())

# Example usage
add_items(apple=3, banana=2, rice=1)
add_items(orange=5, banana=1)
print("Total items:", total_items())
print("Sorted Inventory:")
for item, qty in sorted_inventory():
    print(f"{item}: {qty}")

inventory = {}  # item → (quantity, price)
categories = set()
suppliers = set()

def add_item(item, quantity, price, category, supplier):
    inventory[item] = (quantity, price)
    categories.add(category)
    suppliers.add(supplier)

def remove_item(item):
    if item in inventory:
        del inventory[item]

def update_stock(item, quantity=None, price=None):
    if item in inventory:
        curr_quantity, curr_price = inventory[item]
        inventory[item] = (
            quantity if quantity is not None else curr_quantity,
            price if price is not None else curr_price
        )

def list_by_category(cat):
    return {item: details for item, details in inventory.items() if cat in categories}

def restock_alert(threshold=10):
    return {item: details for item, details in inventory.items() if details[0] < threshold}

# Inventory Management System

class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ₹{self.price} (Qty: {self.quantity})"


class Supplier:
    def __init__(self, name, contact):
        self.__name = name
        self.__contact = contact

    def get_supplier_info(self):
        return f"Supplier: {self.__name}, Contact: {self.__contact}"


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.item_id] = item
        print(f"Added item: {item.name}")

    def update_item(self, item_id, quantity):
        if item_id in self.items:
            self.items[item_id].quantity = quantity
            print(f"Updated quantity of {self.items[item_id].name} to {quantity}")
        else:
            print("Item not found.")

    def remove_item(self, item_id):
        if item_id in self.items:
            removed = self.items.pop(item_id)
            print(f"Removed item: {removed.name}")
        else:
            print("Item not found.")

    def __contains__(self, item_id):
        return item_id in self.items

    def __getitem__(self, item_id):
        return self.items.get(item_id, None)


# ----------------------
# 📌 Sample Usage
# ----------------------

if __name__ == "__main__":
    # Create Inventory
    inventory = Inventory()

    # Add items
    item1 = Item(101, "Laptop", 55000, 10)
    item2 = Item(102, "Keyboard", 850, 25)
    inventory.add_item(item1)
    inventory.add_item(item2)

    # Update quantity
    inventory.update_item(102, 30)

    # Access item using index-like syntax
    print("\nAccessing item by ID 101:")
    print(inventory[101])  # Will call __getitem__

    # Check existence using 'in'
    print("\nIs item 103 in inventory?", 103 in inventory)

    # Remove item
    inventory.remove_item(101)

    # Supplier info (encapsulation)
    supplier = Supplier("Tech Distributors", "9876543210")
    print("\n" + supplier.get_supplier_info())

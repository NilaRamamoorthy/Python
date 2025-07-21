import json
from pretty_display import print_item, print_grouped_items

DATA_FILE = "grocery_data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_item():
    item = input("Enter item name: ")
    category = input("Enter category: ")
    data = load_data()
    data.append({"item": item, "category": category, "bought": False})
    save_data(data)
    print("Item added!")

def remove_item():
    item_name = input("Enter item to remove: ").lower()
    data = load_data()
    new_data = [i for i in data if i["item"].lower() != item_name]
    save_data(new_data)
    print("Item removed!" if len(new_data) != len(data) else "Item not found.")

def mark_bought():
    item_name = input("Enter item to mark as bought: ").lower()
    data = load_data()
    found = False
    for item in data:
        if item["item"].lower() == item_name:
            item["bought"] = True
            found = True
            break
    save_data(data)
    print("Item marked as bought!" if found else "Item not found.")

def search_item():
    keyword = input("Enter keyword to search: ").lower()
    data = load_data()
    results = [item for item in data if keyword in item["item"].lower()]
    if results:
        for item in results:
            print_item(item)
    else:
        print("No items found.")

def show_by_category():
    data = load_data()
    print_grouped_items(data)

def main():
    while True:
        print("\n1. Add Item\n2. Remove Item\n3. Mark as Bought\n4. Search Item\n5. Show by Category\n6. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            mark_bought()
        elif choice == "4":
            search_item()
        elif choice == "5":
            show_by_category()
        elif choice == "6":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()

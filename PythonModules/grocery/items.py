ITEMS = {
    "apple": 40,
    "banana": 10,
    "milk": 50,
    "bread": 25,
    "rice": 70
}

def get_price(item_name):
    return ITEMS.get(item_name.lower(), None)

def show_items():
    print("Available Items:")
    for item, price in ITEMS.items():
        print(f"{item.capitalize()}: ₹{price}")

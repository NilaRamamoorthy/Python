MENU = {
    "Burger": 150,
    "Pizza": 250,
    "Pasta": 200,
    "Coffee": 80,
    "Ice Cream": 100
}

def show_menu():
    print("\n--- Menu ---")
    for item, price in MENU.items():
        print(f"{item}: ₹{price}")

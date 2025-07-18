import random
from restaurant.menu import MENU

def take_order():
    order_id = random.randint(1000, 9999)
    order = {}
    while True:
        item = input("Enter item (or 'done' to finish): ").title()
        if item == 'Done':
            break
        if item in MENU:
            qty = int(input(f"Enter quantity for {item}: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("Item not in menu.")
    return order_id, order

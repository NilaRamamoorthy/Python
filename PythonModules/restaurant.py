from restaurant.menu import show_menu
from restaurant.order import take_order
from restaurant.bill import generate_bill

def main():
    show_menu()
    order_id, order = take_order()
    if order:
        generate_bill(order_id, order)
    else:
        print("No items ordered.")

if __name__ == "__main__":
    main()

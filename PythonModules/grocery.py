from grocery.items import show_items, get_price
from grocery.cart import add_to_cart, clear_cart
from grocery.checkout import generate_bill

def main():
    print("Welcome to Grocery Store")
    show_items()
    
    while True:
        item = input("\nEnter item to add (or 'done' to finish): ").lower()
        if item == 'done':
            break
        price = get_price(item)
        if price is not None:
            qty = int(input(f"Enter quantity of {item}: "))
            add_to_cart(item, qty)
        else:
            print("Item not available.")

    generate_bill()
    clear_cart()

if __name__ == "__main__":
    main()

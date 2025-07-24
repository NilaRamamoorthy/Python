# Custom Exception
class ProductExistsError(Exception):
    pass

def shopping_cart():
    cart = {}
    total = 0.0

    print("🛒 Welcome to the Shopping Cart")
    print("Enter 'done' as product name to finish.\n")

    while True:
        try:
            product = input("Enter product name: ").strip()

            if product.lower() == 'done':
                break

            if product in cart:
                raise ProductExistsError(f"⚠️ '{product}' is already in the cart.")

            price_input = input(f"Enter price for '{product}': ").strip()
            price = float(price_input)  # May raise ValueError

            cart[product] = price

        except ValueError:
            print("❌ Invalid price. Please enter a numeric value.")
        except ProductExistsError as pe:
            print(pe)
        finally:
            # Always show current total
            total = sum(cart.values())
            print(f"🧾 Current total: ₹{total:.2f}\n")

    print("\n✅ Final Cart Summary:")
    for item, price in cart.items():
        print(f"- {item}: ₹{price:.2f}")
    print(f"💰 Total Amount: ₹{total:.2f}")

# Run the cart calculator
shopping_cart()

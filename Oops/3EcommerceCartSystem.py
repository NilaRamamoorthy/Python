# Product class
class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount  # in percentage

    def get_price_after_discount(self):
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        return f"{self.name} - ₹{self.price} (-{self.discount}%)"

# User class
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"

# Cart class
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)

    def total_cost(self):
        return sum(p.get_price_after_discount() for p in self.items)

    @staticmethod
    def calculate_tax(amount):
        return amount * 0.18  # 18% GST

    def __add__(self, product):  # allows cart + product
        self.add_product(product)
        return self

    def __getitem__(self, index):  # allows cart[0]
        return self.items[index]

    def __contains__(self, product):  # allows `product in cart`
        return product in self.items

    def __str__(self):
        return "\n".join([str(p) for p in self.items]) if self.items else "Cart is empty"

# Order class
class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.total = cart.total_cost()
        self.tax = Cart.calculate_tax(self.total)
        self.grand_total = self.total + self.tax

    def show_invoice(self):
        print(f"\nOrder Invoice for {self.user.name}")
        print("-" * 30)
        print(self.cart)
        print("-" * 30)
        print(f"Subtotal      : ₹{self.total:.2f}")
        print(f"Tax (18%)     : ₹{self.tax:.2f}")
        print(f"Grand Total   : ₹{self.grand_total:.2f}")
        print("-" * 30)
# Create user and cart
user = User("Nila", "U001")
cart = Cart()

# Create products
p1 = Product("Python Book", 500, 10)
p2 = Product("USB Drive", 800, 5)
p3 = Product("Headphones", 1500, 20)

# Add products using + and method
cart + p1
cart.add_product(p2)
cart + p3

# Access and check
print("\nCart Contents:")
print(cart)
print("\nFirst item in cart:", cart[0])
print("Is USB Drive in cart?", p2 in cart)

# Place order
order = Order(user, cart)
order.show_invoice()

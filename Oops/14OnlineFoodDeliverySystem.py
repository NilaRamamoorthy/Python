# Online Food Delivery System

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"


class Customer(User):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def __str__(self):
        return f"Customer: {self.name}, Address: {self.address}"


class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu  # Dictionary {item: price}

    def show_menu(self):
        print(f"\nMenu at {self.name}:")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")


class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items  # list of item names
        self.total = sum([restaurant.menu[item] for item in items])

    def show_order(self):
        print(f"\nOrder for {self.customer.name}:")
        for item in self.items:
            print(f"- {item} - ₹{self.restaurant.menu[item]}")
        print(f"Total: ₹{self.total}")


class Delivery:
    def __init__(self, method):
        self.method = method

    def deliver(self):
        print(f"Delivering using: {self.method}")


class ExpressDelivery(Delivery):
    def deliver(self):
        print(f"Express Delivery - Estimated time: 30 mins")

class StandardDelivery(Delivery):
    def deliver(self):
        print(f"Standard Delivery - Estimated time: 1 hour")


# ----------------------
# 📌 Sample Usage
# ----------------------

if __name__ == "__main__":
    # Customer creation
    cust1 = Customer("Ananya", "45, MG Road")
    print(cust1)

    # Restaurant and menu
    dominos = Restaurant("Domino's", {
        "Pizza": 250,
        "Pasta": 150,
        "Garlic Bread": 120
    })
    dominos.show_menu()

    # Place order
    order1 = Order(cust1, dominos, ["Pizza", "Garlic Bread"])
    order1.show_order()

    # Assign delivery method
    delivery1 = ExpressDelivery("Bike")
    delivery1.deliver()

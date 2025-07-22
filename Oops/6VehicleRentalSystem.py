class Vehicle:
    def __init__(self, reg_number, brand, rate_per_day):
        self.reg_number = reg_number
        self.brand = brand
        self.rate_per_day = rate_per_day
        self.__available = True  # encapsulated

    def calculate_rent(self, days):
        return self.rate_per_day * days

    def is_available(self):
        return self.__available

    def mark_rented(self):
        self.__available = False

    def mark_returned(self):
        self.__available = True

    def __str__(self):
        status = "Available" if self.__available else "Rented"
        return f"{self.brand} [{self.reg_number}] - ₹{self.rate_per_day}/day ({status})"


class Car(Vehicle):
    def __init__(self, reg_number, brand, rate_per_day, seats):
        super().__init__(reg_number, brand, rate_per_day)
        self.seats = seats

    def calculate_rent(self, days):
        # Flat rate, but with seat tax
        base = super().calculate_rent(days)
        return base + (self.seats * 50)


class Bike(Vehicle):
    def __init__(self, reg_number, brand, rate_per_day, helmet_required=True):
        super().__init__(reg_number, brand, rate_per_day)
        self.helmet_required = helmet_required

    def calculate_rent(self, days):
        return super().calculate_rent(days) - 50  # small discount


class Customer:
    def __init__(self, name, license_no):
        self.name = name
        self.license_no = license_no

    def __str__(self):
        return f"Customer: {self.name} (License: {self.license_no})"


class Rental:
    def __init__(self, customer, vehicle, days):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days
        self.total = self.vehicle.calculate_rent(days)
        self.vehicle.mark_rented()

    def end_rental(self):
        self.vehicle.mark_returned()

    def __str__(self):
        return (f"{self.customer}\n"
                f"Rented: {self.vehicle}\n"
                f"Duration: {self.days} days\n"
                f"Total: ₹{self.total}")
if __name__ == "__main__":
    # Create vehicles
    car1 = Car("TN01AB1234", "Toyota", 1200, 5)
    bike1 = Bike("TN02XY5678", "Hero", 400)

    # Create a customer
    cust1 = Customer("Nila", "DL12345TN")

    # Rent the car for 3 days
    rental1 = Rental(cust1, car1, 3)

    print(rental1)
    print("\nIs car still available?", car1.is_available())

    # End the rental
    rental1.end_rental()
    print("Car returned.")
    print("Is car available now?", car1.is_available())

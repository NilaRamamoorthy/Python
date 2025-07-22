# Parcel Tracking System

import random

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Sender(Person):
    pass


class Receiver(Person):
    pass


class Tracking:
    used_ids = set()

    @staticmethod
    def validate_tracking_id(tracking_id):
        return tracking_id in Tracking.used_ids

    @classmethod
    def generate_tracking_id(cls):
        while True:
            tid = "TRK" + str(random.randint(10000, 99999))
            if tid not in cls.used_ids:
                cls.used_ids.add(tid)
                return tid


class Parcel:
    def __init__(self, weight, sender: Sender, receiver: Receiver):
        self.weight = weight
        self.sender = sender
        self.receiver = receiver
        self.tracking_id = Tracking.generate_tracking_id()

    def display_info(self):
        print(f"\n📦 Tracking ID: {self.tracking_id}")
        print(f"Weight: {self.weight} kg")
        print(f"Sender: {self.sender.name}, {self.sender.address}")
        print(f"Receiver: {self.receiver.name}, {self.receiver.address}")
        print(f"✅ ID Valid: {Tracking.validate_tracking_id(self.tracking_id)}")


# ----------------------
# 📌 Sample Usage
# ----------------------

if __name__ == "__main__":
    # Create sender and receiver
    sender = Sender("Anita", "Delhi")
    receiver = Receiver("Kumar", "Chennai")

    # Create a parcel
    parcel = Parcel(3.5, sender, receiver)

    # Display parcel info
    parcel.display_info()

    # Try validating a random invalid ID
    print("\n❌ ID Valid:", Tracking.validate_tracking_id("TRK99999"))

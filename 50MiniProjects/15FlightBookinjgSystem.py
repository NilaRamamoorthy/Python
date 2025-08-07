import json
import random
from functools import wraps

# Decorator to confirm booking before finalizing
def confirm_booking(func):
    @wraps(func)
    def wrapper(self, passenger, seat):
        print(f"Please confirm booking seat {seat} for passenger {passenger.name} (y/n): ", end='')
        ans = input().strip().lower()
        if ans != 'y':
            print("Booking canceled.")
            return False
        return func(self, passenger, seat)
    return wrapper

class SeatAlreadyBookedError(Exception):
    pass

class Passenger:
    def __init__(self, name, passenger_id):
        self.name = name
        self.id = passenger_id

class Flight:
    def __init__(self, flight_number, seats_list):
        self.flight_number = flight_number
        self.seats = seats_list  # list of seat strings e.g. ["A1", "A2",...]
        self.booked = set()      # set of booked seats
        self.bookings = {}       # seat -> Passenger

    @confirm_booking
    def book_seat(self, passenger, seat):
        if seat not in self.seats:
            raise ValueError("Invalid seat")
        if seat in self.booked:
            raise SeatAlreadyBookedError(f"Seat {seat} already booked")
        self.booked.add(seat)
        self.bookings[seat] = passenger
        print(f"Seat {seat} booked for {passenger.name}")
        return True

    def cancel_booking(self, seat):
        if seat in self.booked:
            p = self.bookings.pop(seat)
            self.booked.remove(seat)
            print(f"Booking for {p.name} on seat {seat} canceled")
            return p
        else:
            print(f"No booking exists for seat {seat}")
            return None

    def available_seat_generator(self):
        for seat in self.seats:
            if seat not in self.booked:
                yield seat

    def display_status(self):
        print(f"Flight {self.flight_number} status:")
        for seat in self.seats:
            status = "X" if seat in self.booked else "_"
            print(f"{seat}:{status}", end=' ')
        print("\nBooked seats:", sorted(self.booked))

    def export_bookings(self, filename='bookings.json'):
        out = []
        for seat, passenger in self.bookings.items():
            out.append({'seat': seat, 'passenger_id': passenger.id, 'passenger_name': passenger.name})
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({'flight': self.flight_number, 'bookings': out}, f, indent=2)
        print(f"Bookings exported to {filename}")


if __name__ == "__main__":
    # define seats
    seats = [f"{row}{col}" for row in range(1, 6) for col in ['A', 'B', 'C', 'D']]
    flight = Flight("FL123", seats)

    p1 = Passenger("Alice", "P001")
    p2 = Passenger("Bob", "P002")

    flight.display_status()
    try:
        flight.book_seat(p1, "1A")
        flight.book_seat(p2, "1A")  # triggers error
    except Exception as e:
        print("Error:", e)

    flight.display_status()

    print("Available seats:")
    for seat in flight.available_seat_generator():
        print(seat, end=' ')
    print()

    flight.cancel_booking("1A")
    flight.export_bookings()
    flight.display_status()

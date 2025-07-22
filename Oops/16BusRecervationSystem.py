# Bus Reservation System

class Seat:
    def __init__(self, seat_no):
        self.seat_no = seat_no
        self.is_booked = False

    def book(self):
        self.is_booked = True

    def cancel(self):
        self.is_booked = False

    def __str__(self):
        return f"Seat {self.seat_no} - {'Booked' if self.is_booked else 'Available'}"


class Passenger:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"{self.name} ({self.contact})"


class Booking:
    def __init__(self, passenger, seat):
        self.passenger = passenger
        self.seat = seat
        self.seat.book()

    def cancel(self):
        self.seat.cancel()

    def __eq__(self, other):
        return self.seat.seat_no == other.seat.seat_no

    def __str__(self):
        return f"Booking: {self.passenger} - {self.seat}"


class Bus:
    def __init__(self, bus_no, total_seats):
        self.bus_no = bus_no
        self.seats = [Seat(i + 1) for i in range(total_seats)]
        self.bookings = []

    def check_availability(self):
        return [seat for seat in self.seats if not seat.is_booked]

    def book_seat(self, passenger, seat_no):
        if 1 <= seat_no <= len(self.seats):
            seat = self.seats[seat_no - 1]
            if seat.is_booked:
                print(f"Seat {seat_no} is already booked.")
            else:
                booking = Booking(passenger, seat)
                self.bookings.append(booking)
                print("Booking successful.")
        else:
            print("Invalid seat number.")

    def cancel_booking(self, seat_no):
        for booking in self.bookings:
            if booking.seat.seat_no == seat_no:
                booking.cancel()
                self.bookings.remove(booking)
                print(f"Booking for seat {seat_no} cancelled.")
                return
        print("Booking not found.")

    def show_bookings(self):
        if not self.bookings:
            print("No bookings yet.")
        else:
            for booking in self.bookings:
                print(booking)


# ----------------------
# 📌 Sample Usage
# ----------------------

if __name__ == "__main__":
    bus = Bus("KA09AB1234", 5)

    # Creating passengers
    p1 = Passenger("Arjun", "9999911111")
    p2 = Passenger("Meena", "8888822222")

    # Booking seats
    bus.book_seat(p1, 1)
    bus.book_seat(p2, 3)

    # Showing all bookings
    print("\nCurrent Bookings:")
    bus.show_bookings()

    # Cancel a booking
    print("\nCancelling seat 1...")
    bus.cancel_booking(1)

    # Show availability
    print("\nAvailable Seats:")
    for seat in bus.check_availability():
        print(seat)

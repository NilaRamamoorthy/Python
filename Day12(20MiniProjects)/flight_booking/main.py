# main.py

from flight.booking import book_flight, view_bookings, list_destinations
from flight.payment import make_payment

# Book flights
book_flight(7001, "Alice", "Paris", "AF203")
book_flight(7002, "Bob", "New York", "UA101")
book_flight(7001, "Alice", "Rome", "AZ303")  # Duplicate

# Make payments
make_payment(7001)
make_payment(7003)  # Invalid ID

# View bookings and destinations
view_bookings()
list_destinations()

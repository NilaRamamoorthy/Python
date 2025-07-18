# booking.py

# Dictionary to hold flight bookings
bookings = {}

# Set to track unique destinations
destinations = set()

def book_flight(passenger_id, name, destination, flight_number):
    key = (passenger_id,)
    if key in bookings:
        print(f"Passenger {name} already has a booking.\n")
        return

    bookings[key] = {
        "name": name,
        "destination": destination,
        "flight_number": flight_number,
        "paid": False
    }

    destinations.add(destination)
    print(f"Booking confirmed for {name} to {destination} on flight {flight_number}.\n")

def view_bookings():
    print("✈️ Current Bookings:")
    for pid, data in bookings.items():
        status = "Paid" if data["paid"] else "Pending"
        print(f"ID: {pid}, Name: {data['name']}, Destination: {data['destination']}, Flight: {data['flight_number']}, Status: {status}")
    print()

def list_destinations():
    print("Unique Destinations Booked:")
    print(", ".join(destinations), "\n")

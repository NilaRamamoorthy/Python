# Initial flight data
flights = {
    "AI101": {"route": "Delhi to Mumbai", "passengers": ["Alice", "Bob"]},
    "AI102": {"route": "Mumbai to Chennai", "passengers": []}
}

MAX_SEATS = 3

# 1. Add passenger
def book_seat(flight_id, name):
    flight = flights.setdefault(flight_id, {"route": "Unknown", "passengers": []})
    if len(flight["passengers"]) < MAX_SEATS:
        flight["passengers"].append(name)
        print(f"{name} booked on flight {flight_id}.")
    else:
        print(f"Flight {flight_id} is full.")

# 2. Remove passenger
def cancel_seat(flight_id, name):
    if flight_id in flights and name in flights[flight_id]["passengers"]:
        flights[flight_id]["passengers"].remove(name)
        print(f"{name}'s booking on flight {flight_id} cancelled.")
    else:
        print(f"Passenger not found on flight {flight_id}.")

# Operations
book_seat("AI101", "Charlie")
book_seat("AI101", "David")  # should exceed max
cancel_seat("AI101", "Bob")

# Display flight status
print("\nFlight Bookings:")
for fid, data in flights.items():
    print(f"{fid} ({data['route']}): {data['passengers']}")

# bus_ops.py

seat_info = {}  # { (user_id, seat_no): {"name": ..., "route": ...} }
occupied_seats = set()  # to avoid duplicate bookings

def reserve_seat(user_id, seat_no, name, route):
    if seat_no in occupied_seats:
        return f"❌ Seat {seat_no} is already booked."
    key = (user_id, seat_no)
    seat_info[key] = {"name": name, "route": route}
    occupied_seats.add(seat_no)
    return f"✅ Seat {seat_no} successfully booked for {name}."

def cancel_seat(user_id, seat_no):
    key = (user_id, seat_no)
    if key in seat_info:
        del seat_info[key]
        occupied_seats.discard(seat_no)
        return f"🔄 Seat {seat_no} booking cancelled."
    return "⚠️ Booking not found."

def display_bookings():
    print("\n🚌 Current Bookings:")
    for key, value in seat_info.items():
        print(f"User ID: {key[0]}, Seat: {key[1]}, Name: {value['name']}, Route: {value['route']}")
    print(f"\nTotal Occupied Seats: {len(occupied_seats)} - {occupied_seats}")

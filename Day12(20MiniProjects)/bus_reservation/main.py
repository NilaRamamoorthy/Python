# main.py

from bus_ops import reserve_seat, cancel_seat, display_bookings

print(reserve_seat("user101", "A1", "Ravi", "Chennai to Coimbatore"))
print(reserve_seat("user102", "A2", "Priya", "Chennai to Madurai"))
print(reserve_seat("user103", "A1", "Arun", "Chennai to Salem"))  # Duplicate seat

print(cancel_seat("user101", "A1"))
print(reserve_seat("user104", "A1", "Divya", "Chennai to Trichy"))

display_bookings()

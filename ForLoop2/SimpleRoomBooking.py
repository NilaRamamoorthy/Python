rooms = {"single": 1000, "double": 1800, "suite": 2500}
room_type = input("Enter room type: ").lower()
nights = int(input("Enter number of nights: "))

if room_type in rooms:
    total = rooms[room_type] * nights
    if nights > 3:
        total *= 0.9
    print(f"Total price: ₹{total:.2f}")
else:
    print("Invalid room type")
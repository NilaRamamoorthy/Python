# 16. Room Booking Price Calculator
room_type = input("Enter room type (Standard/Deluxe): ").lower()
nights = int(input("Enter number of nights: "))
rate = 1000 if room_type == "standard" else 1500 if room_type == "deluxe" else 0
if rate:
    total = rate * nights
    if nights > 3:
        total *= 0.8
    print(f"Total price: ₹{total:.2f}")
else:
    print("Invalid room type")
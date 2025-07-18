# payment.py

from flight.booking import bookings

def make_payment(passenger_id):
    key = (passenger_id,)
    if key not in bookings:
        print("Booking not found.\n")
        return
    if bookings[key]["paid"]:
        print("Payment already made.\n")
        return

    bookings[key]["paid"] = True
    print(f"Payment completed for {bookings[key]['name']}.\n")

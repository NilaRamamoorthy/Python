from datetime import datetime

# Custom Exception
class OverBookingError(Exception):
    pass

# Booking Function
def book_hotel():
    total_rooms = 5

    try:
        name = input("Enter your name: ")

        date_input = input("Enter check-in date (YYYY-MM-DD): ")
        check_in = datetime.strptime(date_input, "%Y-%m-%d")
        assert check_in.date() >= datetime.today().date(), "Date must be today or later"

        guests = input("Enter number of guests: ")
        guests = int(guests)
        assert guests > 0, "Guest count must be positive"

        if guests > total_rooms:
            raise OverBookingError(f"Only {total_rooms} rooms available, but {guests} guests requested.")

    except ValueError:
        print("❌ Invalid date format or non-numeric input.")
    except AssertionError as ae:
        print(f"❌ Assertion Error: {ae}")
    except OverBookingError as oe:
        print(f"❌ Booking Error: {oe}")
    else:
        print(f"✅ Booking confirmed for {name} on {check_in.strftime('%Y-%m-%d')} for {guests} guests.")
    finally:
        print("📌 Booking process complete.")

# Run Booking
book_hotel()

import logging
from datetime import datetime

# Setup logger
logging.basicConfig(filename="booking_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Custom Exceptions
class NoSeatsAvailableError(Exception):
    pass

class FrequentFlyerBookingError(Exception):
    pass

# Booking system class
class FlightBookingSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked = 0
        self.frequent_flyers = set(["FF123", "FF999"])  # example frequent flyer IDs

    def book_ticket(self, name, user_id, date_str):
        try:
            if self.booked >= self.total_seats:
                raise NoSeatsAvailableError("No seats available!")

            if user_id in self.frequent_flyers:
                raise FrequentFlyerBookingError(f"Special booking required for frequent flyer ID: {user_id}")

            # Validate date
            datetime.strptime(date_str, "%Y-%m-%d")

            self.booked += 1
            print(f"✅ Ticket booked for {name}. Booking ID: {user_id}")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")
        except NoSeatsAvailableError as e:
            print(f"❌ {e}")
        except FrequentFlyerBookingError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        finally:
            logging.info(f"Attempted booking: Name={name}, ID={user_id}, Date={date_str}, Booked={self.booked}")

# Simulation
system = FlightBookingSystem(total_seats=2)

# Sample loop to book tickets
for _ in range(4):
    print("\n--- New Booking ---")
    name = input("Enter your name: ")
    user_id = input("Enter your ID: ")
    date = input("Enter travel date (YYYY-MM-DD): ")
    system.book_ticket(name, user_id, date)

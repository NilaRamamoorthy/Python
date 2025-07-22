class Movie:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre

    def __str__(self):
        return f"{self.title} ({self.genre}) - {self.duration} mins"


class Seat:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked = 0

    def book_seat(self, count=1):
        if Seat.is_available(self, count):
            self.booked += count
            return True
        return False

    def cancel_seat(self, count=1):
        if self.booked >= count:
            self.booked -= count
            return True
        return False

    @staticmethod
    def is_available(seat_obj, count=1):
        return (seat_obj.total_seats - seat_obj.booked) >= count


class Ticket:
    def __init__(self, movie, user_name, seat_count):
        self.movie = movie
        self.user_name = user_name
        self.seat_count = seat_count

    def __str__(self):
        return f"Ticket for {self.movie.title} | Booked by: {self.user_name} | Seats: {self.seat_count}"


class User:
    def __init__(self, name):
        self.name = name
        self.tickets = []

    def book_ticket(self, movie, seat_obj, seat_count):
        if seat_obj.book_seat(seat_count):
            ticket = Ticket(movie, self.name, seat_count)
            self.tickets.append(ticket)
            print(f"Booking successful:\n{ticket}")
        else:
            print("Booking failed: Not enough seats.")

    def cancel_ticket(self, ticket, seat_obj):
        if ticket in self.tickets:
            seat_obj.cancel_seat(ticket.seat_count)
            self.tickets.remove(ticket)
            print("Ticket cancelled:", ticket)
if __name__ == "__main__":
    m1 = Movie("Interstellar", 169, "Sci-Fi")
    m2 = Movie("Inception", 148, "Thriller")

    seat_m1 = Seat(50)
    user1 = User("Alice")

    user1.book_ticket(m1, seat_m1, 2)
    user1.book_ticket(m1, seat_m1, 49)  # Will fail
    for ticket in user1.tickets:
        print(ticket)

    user1.cancel_ticket(user1.tickets[0], seat_m1)

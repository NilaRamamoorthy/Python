# 15. Movie Theater Booking
seats = (
    ('A1', 'A2', 'A3'),
    ('B1', 'B2', None),
    ('C1', None, 'C3')
)
for row in seats:
    for seat in row:
        if seat is None:
            print("Empty seat found")
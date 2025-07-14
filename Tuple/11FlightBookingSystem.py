# 11. Flight Booking System
flights = [
    ('AI101', 'Delhi', 'Mumbai', ('Alice', 'Bob')),
    ('6E202', 'Bangalore', 'Chennai', ('Charlie', 'David', 'Eve'))
]
for fid, src, dest, passengers in flights:
    print(f"Flight {fid} from {src} to {dest}, Passengers: {len(passengers)}")
    for p in passengers:
        print(" -", p)

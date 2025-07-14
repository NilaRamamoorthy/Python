# 17. Festival Event Planner
events = [
    ('Dance Show', ('18:00', '20:00', 'Stage A')),
    ('Magic Show', ('20:00', '21:00', 'Stage B'))
]
for event, (start, end, location) in events:
    print(f"{event}: {start} to {end} at {location}")

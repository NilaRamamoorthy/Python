# 8. Bus Schedule Management System
buses = [
    ('KA01AB1234', '08:00', '12:00', ('Stop1', 'Stop2', 'Stop3')),
    ('KA01XY5678', '09:30', '13:30', ('StopA', 'StopB', 'StopC'))
]
for bus_no, dep, arr, stops in buses:
    print(f"Bus {bus_no}: {dep} to {arr}, Stops: {', '.join(stops)}")



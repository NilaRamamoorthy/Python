# main.py

from traffic_control import set_signal, get_signal, display_all_signals

set_signal("Central Square", "08:00 AM", "RED")
set_signal("Central Square", "08:30 AM", "GREEN")
set_signal("Park Avenue", "08:00 AM", "YELLOW")
set_signal("Main Street", "09:00 AM", "RED")

print(f"Signal at Central Square at 08:00 AM: {get_signal('Central Square', '08:00 AM')}")
print(f"Signal at Park Avenue at 09:00 AM: {get_signal('Park Avenue', '09:00 AM')}")

display_all_signals()

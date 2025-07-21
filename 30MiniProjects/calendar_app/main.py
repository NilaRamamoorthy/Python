# main.py

from event_ops import add_event, delete_event, update_event
from calendar_view import get_dates_with_events, list_events_on_date

# Sample usage
add_event("2025-07-21", "10:00", "Team Meeting", {"Alice", "Bob"})
add_event("2025-07-22", "14:00", "Doctor Appointment", {"Alice"})
update_event("2025-07-21", "10:00", new_desc="Project Kickoff")
delete_event("2025-07-22", "14:00")

print("\nDates with Events:")
print(get_dates_with_events())

print("\nEvents on 2025-07-21:")
list_events_on_date("2025-07-21")

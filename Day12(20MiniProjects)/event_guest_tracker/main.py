# main.py

from guest_utils import create_event, add_guest, update_rsvp, view_guests, view_rsvp

# Creating an event
print(create_event(("EVT2025",)))

# Adding guests
print(add_guest(("EVT2025",), "Aarav"))
print(add_guest(("EVT2025",), "Divya"))
print(add_guest(("EVT2025",), "Riya"))
print(add_guest(("EVT2025",), "Aarav"))  # Duplicate will be ignored by set

# Updating RSVP
print(update_rsvp(("EVT2025",), "Aarav", "Yes"))
print(update_rsvp(("EVT2025",), "Riya", "Maybe"))

# Viewing guest list and RSVPs
print("\n" + view_guests(("EVT2025",)))
print("\n" + view_rsvp(("EVT2025",)))

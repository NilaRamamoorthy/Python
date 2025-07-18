# guest_utils.py

event_data = {}  # {(event_id): {"guests": set(), "rsvp": {guest_name: status}} }

def create_event(event_id):
    if event_id not in event_data:
        event_data[event_id] = {"guests": set(), "rsvp": {}}
        return f"✅ Event {event_id} created."
    return "⚠️ Event already exists."

def add_guest(event_id, guest_name):
    if event_id not in event_data:
        return "❌ Event not found."
    event_data[event_id]["guests"].add(guest_name)
    return f"✅ Guest '{guest_name}' added to event {event_id}."

def update_rsvp(event_id, guest_name, status):
    if event_id not in event_data:
        return "❌ Event not found."
    if guest_name not in event_data[event_id]["guests"]:
        return "⚠️ Guest not found in this event."
    event_data[event_id]["rsvp"][guest_name] = status
    return f"📨 RSVP updated: {guest_name} - {status}"

def view_guests(event_id):
    if event_id not in event_data:
        return "❌ Event not found."
    return f"🎉 Guests for {event_id}: {', '.join(event_data[event_id]['guests'])}"

def view_rsvp(event_id):
    if event_id not in event_data:
        return "❌ Event not found."
    return f"📋 RSVP Status:\n" + '\n'.join([f"{g}: {s}" for g, s in event_data[event_id]["rsvp"].items()])

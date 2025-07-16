# Initial event data
events = {
    "Tech Talk": {"participants": ["Alice", "Bob"], "max": 3},
    "Workshop": {"participants": ["Charlie"], "max": 2}
}

# 1. Register participant
def register(event_name, person):
    event = events.get(event_name)
    if event:
        if len(event["participants"]) < event["max"]:
            event["participants"].append(person)
            print(f"{person} registered for {event_name}.")
        else:
            print(f"{event_name} is full.")
    else:
        print(f"Event '{event_name}' does not exist.")

# 2. Cancel registration
def cancel(event_name, person):
    if event_name in events and person in events[event_name]["participants"]:
        events[event_name]["participants"].remove(person)
        print(f"{person} removed from {event_name}.")
    else:
        print(f"{person} is not registered for {event_name}.")

# 3. Count participants
print("Event Status:")
for event, data in events.items():
    print(f"{event}: {len(data['participants'])}/{data['max']} participants")

# Perform operations
register("Tech Talk", "Charlie")
register("Tech Talk", "David")  # should exceed max
cancel("Workshop", "Charlie")

print("\nUpdated Event Status:")
for event, data in events.items():
    print(f"{event}: {data['participants']} ({len(data['participants'])}/{data['max']})")

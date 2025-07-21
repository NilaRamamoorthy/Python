trips = []

def add_trip(destination, dates, participants, itinerary):
    trip = {
        "destination": destination,
        "dates": dates,
        "participants": set(participants),
        "itinerary": itinerary
    }
    trips.append(trip)

def edit_trip(index, key, value):
    if key == "participants":
        trips[index][key] = set(value)
    elif key == "dates":
        trips[index][key] = tuple(value)
    else:
        trips[index][key] = value

def remove_trip(index):
    if 0 <= index < len(trips):
        trips.pop(index)

def list_unique_destinations():
    return set(trip['destination'] for trip in trips)

def calculate_cost(index, cost_per_person):
    return cost_per_person * len(trips[index]['participants'])

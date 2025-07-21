# event_ops.py

from typing import List, Dict, Set, Tuple

# Global event list and IDs
events: List[Dict] = []
event_ids: Set[Tuple[str, str]] = set()  # (date, time) as immutable ID

def add_event(date: str, time: str, desc: str, participants: Set[str]):
    event_id = (date, time)
    if event_id in event_ids:
        print("Event already exists at this date and time.")
        return
    event = {"date": date, "time": time, "desc": desc, "participants": participants}
    events.append(event)
    event_ids.add(event_id)
    print("Event added.")

def delete_event(date: str, time: str):
    event_id = (date, time)
    for e in events:
        if e["date"] == date and e["time"] == time:
            events.remove(e)
            event_ids.remove(event_id)
            print("Event deleted.")
            return
    print("Event not found.")

def update_event(date: str, time: str, new_desc: str = None, new_participants: Set[str] = None):
    for e in events:
        if e["date"] == date and e["time"] == time:
            if new_desc:
                e["desc"] = new_desc
            if new_participants:
                e["participants"] = new_participants
            print("Event updated.")
            return
    print("Event not found.")

def get_all_events() -> List[Dict]:
    return events

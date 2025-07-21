# calendar_view.py

from typing import List, Set, Dict
from event_ops import get_all_events

def get_dates_with_events() -> Set[str]:
    return {event["date"] for event in get_all_events()}

def list_events_on_date(date: str):
    print(f"Events on {date}:")
    found = False
    for event in get_all_events():
        if event["date"] == date:
            print(f" - {event['time']} | {event['desc']} | Participants: {', '.join(event['participants'])}")
            found = True
    if not found:
        print("No events on this date.")

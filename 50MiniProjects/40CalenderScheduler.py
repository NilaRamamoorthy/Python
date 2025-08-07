import os
from datetime import datetime
from icalendar import Calendar, Event as ICalEvent
from typing import List, Generator
import functools

# Decorator to convert datetime to human-readable format
def human_readable(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        dt = func(*args, **kwargs)
        return dt.strftime("%A, %B %d, %Y at %I:%M %p")
    return wrapper

# Event class to represent a calendar event
class Event:
    def __init__(self, summary: str, start: datetime, end: datetime, location: str = "", description: str = ""):
        self.summary = summary
        self.start = start
        self.end = end
        self.location = location
        self.description = description

    def to_ical(self) -> ICalEvent:
        event = ICalEvent()
        event.add('summary', self.summary)
        event.add('dtstart', self.start)
        event.add('dtend', self.end)
        event.add('location', self.location)
        event.add('description', self.description)
        return event

# CalendarScheduler class to manage events
class CalendarScheduler:
    def __init__(self, filename: str):
        self.filename = filename
        self.calendar = Calendar(version="2.0", prodid="-//My Company//NONSGML Event//EN")
        self.events_by_date = {}

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                self.calendar = Calendar.from_ical(f.read())
            self._index_events()

    def save(self):
        with open(self.filename, 'wb') as f:
            f.write(self.calendar.to_ical())

    def add_event(self, event: Event):
        ical_event = event.to_ical()
        self.calendar.add_component(ical_event)
        self._index_event(event)

    def _index_event(self, event: Event):
        date_str = event.start.date().isoformat()
        if date_str not in self.events_by_date:
            self.events_by_date[date_str] = []
        self.events_by_date[date_str].append(event)

    def _index_events(self):
        for component in self.calendar.walk('vevent'):
            event = Event(
                summary=component.get('summary'),
                start=component.get('dtstart').dt,
                end=component.get('dtend').dt,
                location=component.get('location', ''),
                description=component.get('description', '')
            )
            self._index_event(event)

    @human_readable
    def get_event_start(self, event: Event) -> datetime:
        return event.start

    def get_events_for_day(self, date: datetime) -> Generator[Event, None, None]:
        date_str = date.date().isoformat()
        for event in self.events_by_date.get(date_str, []):
            yield event

    def check_time_conflict(self, new_event: Event) -> bool:
        for event in self.get_events_for_day(new_event.start):
            if (new_event.start < event.end and new_event.end > event.start):
                return True
        return False

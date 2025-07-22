# Conference Registration System

class Attendee:
    count = 0  # Class-level attribute

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Attendee.count += 1

    @classmethod
    def total_attendees(cls):
        return cls.count


class Session:
    def __init__(self, topic, speaker):
        self.topic = topic
        self.speaker = speaker

    def __str__(self):
        return f"{self.topic} by {self.speaker}"


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def list_sessions(self):
        return [str(session) for session in self.sessions]


class Registration:
    def __init__(self, attendee, event):
        self.attendee = attendee  # Aggregation
        self.event = event
        self.assigned_sessions = []

    def assign_session(self, session):
        self.assigned_sessions.append(session)

    def show_registration(self):
        print(f"\n📋 Registration for {self.attendee.name} ({self.attendee.email})")
        print(f"Event: {self.event.name} on {self.event.date}")
        print("Sessions Assigned:")
        for sess in self.assigned_sessions:
            print("  🔹", sess)

# ----------------------
# 📌 Sample Usage
# ----------------------

if __name__ == "__main__":
    # Create Event
    conf_event = Event("Tech Summit 2025", "2025-11-10")

    # Add Sessions
    s1 = Session("AI in Healthcare", "Dr. Mehta")
    s2 = Session("Future of Blockchain", "Mr. Kumar")
    s3 = Session("Ethical Hacking 101", "Ms. Riya")
    conf_event.add_session(s1)
    conf_event.add_session(s2)
    conf_event.add_session(s3)

    # Create Attendees
    a1 = Attendee("Aarav", "aarav@mail.com")
    a2 = Attendee("Tanya", "tanya@mail.com")

    # Register them
    r1 = Registration(a1, conf_event)
    r1.assign_session(s1)
    r1.assign_session(s2)

    r2 = Registration(a2, conf_event)
    r2.assign_session(s3)

    # Show Registration Details
    r1.show_registration()
    r2.show_registration()

    # Total Attendees
    print("\n👥 Total Attendees Registered:", Attendee.total_attendees())

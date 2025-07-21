appointments = {}  # Dict: date → list of tuples: (time, person, purpose)
people = set()

def add_appointment(date, time, person, purpose):
    people.add(person)
    if date not in appointments:
        appointments[date] = []
    appointments[date].append((time, person, purpose))

def edit_appointment(date, old_time, new_time=None, new_person=None, new_purpose=None):
    if date in appointments:
        for idx, (time, person, purpose) in enumerate(appointments[date]):
            if time == old_time:
                new_entry = (
                    new_time if new_time else time,
                    new_person if new_person else person,
                    new_purpose if new_purpose else purpose
                )
                appointments[date][idx] = new_entry
                return True
    return False

def remove_appointment(date, time):
    if date in appointments:
        appointments[date] = [appt for appt in appointments[date] if appt[0] != time]
        if not appointments[date]:
            del appointments[date]

def display_schedule():
    for date in sorted(appointments):
        print(f"\nDate: {date}")
        for time, person, purpose in sorted(appointments[date]):
            print(f"  {time} - {person}: {purpose}")

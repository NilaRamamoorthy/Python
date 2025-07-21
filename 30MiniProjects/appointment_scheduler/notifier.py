def notify_upcoming(appointments, today):
    print(f"\nReminders for {today}:")
    if today in appointments:
        for time, person, purpose in appointments[today]:
            print(f"  Reminder: {person} has '{purpose}' at {time}")
    else:
        print("  No appointments today.")

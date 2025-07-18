# timetable_utils.py

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods = ["Period 1", "Period 2", "Period 3", "Period 4"]

# Sample subject pool
available_subjects = {"Math", "Physics", "Chemistry", "Biology", "English", "Computer"}

# Dictionary to store schedule using (day, period) as key
timetable = {}

def assign_subjects():
    for day in days:
        used_subjects = set()  # reset per day
        for i, period in enumerate(periods):
            for subject in available_subjects:
                if subject not in used_subjects:
                    timetable[(day, period)] = subject
                    used_subjects.add(subject)
                    break

def display_timetable():
    print("\nCollege Timetable:")
    for day in days:
        print(f"\n{day}")
        for period in periods:
            subject = timetable.get((day, period), "Free")
            print(f"  {period}: {subject}")

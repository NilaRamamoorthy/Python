# activity_ops.py

from typing import List, Dict

# List of activity dictionaries
activities: List[Dict] = []

def add_activity(date: str, activity_type: str, duration: int, calories: int):
    activity = {
        "date": date,
        "type": activity_type.lower(),
        "duration": duration,
        "calories": calories
    }
    activities.append(activity)
    print(f"Activity '{activity_type}' added for {date}.")

def edit_activity(index: int, activity_type: str = None, duration: int = None, calories: int = None):
    if 0 <= index < len(activities):
        if activity_type:
            activities[index]["type"] = activity_type.lower()
        if duration:
            activities[index]["duration"] = duration
        if calories:
            activities[index]["calories"] = calories
        print("Activity updated.")
    else:
        print("Invalid activity index.")

def get_all_activities() -> List[Dict]:
    return activities

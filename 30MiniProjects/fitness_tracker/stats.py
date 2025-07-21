# stats.py

from typing import Dict, List
from activity_ops import get_all_activities

def group_by_activity_type() -> Dict[str, List[Dict]]:
    grouped: Dict[str, List[Dict]] = {}
    for act in get_all_activities():
        grouped.setdefault(act["type"], []).append(act)
    return grouped

def unique_activities() -> set:
    return {act["type"] for act in get_all_activities()}

def show_stats():
    grouped = group_by_activity_type()
    for act_type, records in grouped.items():
        total_duration = sum(r["duration"] for r in records)
        total_calories = sum(r["calories"] for r in records)
        print(f"{act_type.title()} → Duration: {total_duration} mins, Calories: {total_calories}")

def evaluate_goals(daily_goal_calories: int):
    calories_by_date: Dict[str, int] = {}
    for act in get_all_activities():
        calories_by_date.setdefault(act["date"], 0)
        calories_by_date[act["date"]] += act["calories"]

    for date, total in calories_by_date.items():
        status = "✅ Goal Met" if total >= daily_goal_calories else "❌ Goal Not Met"
        print(f"{date}: {total} cal – {status}")

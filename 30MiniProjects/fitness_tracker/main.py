# main.py

from activity_ops import add_activity, edit_activity
from stats import show_stats, evaluate_goals, unique_activities

# Adding activities
add_activity("2025-07-20", "Running", 30, 300)
add_activity("2025-07-20", "Cycling", 45, 350)
add_activity("2025-07-21", "Yoga", 60, 200)

# Editing an activity
edit_activity(2, duration=70)

# Display statistics
print("\nActivity Stats:")
show_stats()

# Unique activity types
print("\nUnique Activities:")
print(unique_activities())

# Evaluate daily calorie goal
print("\nGoal Evaluation (Goal: 500 cal/day):")
evaluate_goals(500)

# Class slots (e.g., "9AM-10AM", "10AM-11AM")
math_class = {"9AM-10AM", "10AM-11AM", "1PM-2PM"}
science_class = {"10AM-11AM", "11AM-12PM", "2PM-3PM"}

# Detect conflicting class times using intersection
conflicts = math_class.intersection(science_class)
print("Conflicting Class Slots:", conflicts)

# Find available slots in math class not used by science class
math_only_slots = math_class.difference(science_class)
print("Available Slots (Only Math):", math_only_slots)

# Suggest an additional slot
suggested_slot = "3PM-4PM"
math_class.add(suggested_slot)
print("Updated Math Class Slots with Suggestion:", math_class)

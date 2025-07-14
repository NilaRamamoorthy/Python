# Daily Meal Planner

# Meal plan for the week
meal_plan = [
    ["Monday", "Idly"],
    ["Tuesday", "Chapati"],
    ["Wednesday", "Rice"],
    ["Thursday", "Pasta"],
    ["Friday", "Dosa"],
    ["Saturday", "Pizza"],
    ["Sunday", "Poori"]
]

# Update a meal
day_to_update = input("Enter the day you want to update: ").strip().title()
new_meal = input(f"Enter new meal for {day_to_update}: ").strip().title()

for meal in meal_plan:
    if meal[0] == day_to_update:
        meal[1] = new_meal
        break
else:
    print("Day not found in meal plan.")

# Remove a meal
day_to_remove = input("Enter a day to remove from meal plan: ").strip().title()
meal_plan = [meal for meal in meal_plan if meal[0] != day_to_remove]

# Slice to view weekend plans
print("\nWeekend Meal Plan:")
for day in meal_plan[-2:]:
    print(f"{day[0]} - {day[1]}")

# Display full meal plan
print("\nFull Weekly Meal Plan:")
for day in meal_plan:
    print(f"{day[0]} - {day[1]}")

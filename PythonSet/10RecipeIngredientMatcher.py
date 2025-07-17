# Ingredients required for a recipe
required_ingredients = {"flour", "sugar", "eggs", "milk", "vanilla", "butter"}

# Ingredients available at home
available_ingredients = {"flour", "sugar", "eggs", "milk"}

# Check if all required ingredients are available
if available_ingredients.issuperset(required_ingredients):
    print("You have all the ingredients to cook the recipe!")
else:
    print("Some ingredients are missing.")

# Find missing ingredients
missing = required_ingredients.difference(available_ingredients)
print("Missing Ingredients:", missing)

# Check if a particular ingredient is available
check_item = "vanilla"
if check_item in available_ingredients:
    print(f"{check_item} is available.")
else:
    print(f"{check_item} is missing.")

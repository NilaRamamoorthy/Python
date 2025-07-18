# recipe_book.py

# Dictionary to store recipes using (title,) as key
recipes = {}

# Set to store all utensils used
all_utensils = set()

def add_recipe(title, ingredients, steps, utensils):
    key = (title,)
    if key in recipes:
        print(f"Recipe '{title}' already exists.\n")
        return

    recipes[key] = {
        "ingredients": ingredients,
        "steps": steps,
        "utensils": set(utensils)  # remove duplicates
    }

    # Update global utensil set
    all_utensils.update(utensils)

    print(f"Recipe '{title}' added successfully.\n")

def view_recipe(title):
    key = (title,)
    if key not in recipes:
        print(f"Recipe '{title}' not found.\n")
        return

    data = recipes[key]
    print(f"--- {title} ---")
    print("Ingredients:")
    for ing in data["ingredients"]:
        print(f" - {ing}")
    print("Steps:")
    for i, step in enumerate(data["steps"], 1):
        print(f" {i}. {step}")
    print("Utensils Needed:", ", ".join(data["utensils"]), "\n")

def list_all_utensils():
    print("All Utensils Used Across Recipes:")
    print(", ".join(all_utensils), "\n")

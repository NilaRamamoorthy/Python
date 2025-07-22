import json
import os

RECIPE_FILE = "recipes.json"

def load_recipes():
    if os.path.exists(RECIPE_FILE):
        with open(RECIPE_FILE, "r") as f:
            return json.load(f)
    return []

def save_recipes(recipes):
    with open(RECIPE_FILE, "w") as f:
        json.dump(recipes, f, indent=4)

def add_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    steps = input("Enter preparation steps: ")

    recipe = {
        "name": name.strip(),
        "ingredients": [ing.strip() for ing in ingredients],
        "steps": steps.strip()
    }

    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    print(f"Recipe '{name}' added successfully.")

def search_recipe():
    name = input("Enter recipe name to search: ").strip().lower()
    recipes = load_recipes()
    found = False
    for r in recipes:
        if r["name"].lower() == name:
            print(f"\nRecipe: {r['name']}")
            print("Ingredients:", ", ".join(r["ingredients"]))
            print("Steps:", r["steps"])
            found = True
            break
    if not found:
        print("Recipe not found.")

def main():
    while True:
        print("\n--- Recipe Book ---")
        print("1. Add Recipe")
        print("2. Search Recipe")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_recipe()
        elif choice == "2":
            search_recipe()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

main()

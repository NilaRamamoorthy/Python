import json

RECIPE_FILE = "recipe_book/recipes.json"

def load_recipes():
    try:
        with open(RECIPE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_recipes(recipes):
    with open(RECIPE_FILE, "w") as file:
        json.dump(recipes, file, indent=4)

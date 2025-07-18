from recipe_book.storage import load_recipes, save_recipes

def add_recipe(name, ingredients, steps):
    recipes = load_recipes()
    new_recipe = {
        "name": name,
        "ingredients": ingredients,
        "steps": steps
    }
    recipes.append(new_recipe)
    save_recipes(recipes)
    print(f"Recipe '{name}' added successfully.")

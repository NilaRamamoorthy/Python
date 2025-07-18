from recipe_book.storage import load_recipes

def search_recipe_by_name(name):
    recipes = load_recipes()
    for recipe in recipes:
        if recipe["name"].lower() == name.lower():
            print(f"\nRecipe: {recipe['name']}")
            print("Ingredients:", ', '.join(recipe['ingredients']))
            print("Steps:", ' -> '.join(recipe['steps']))
            return
    print("Recipe not found.")

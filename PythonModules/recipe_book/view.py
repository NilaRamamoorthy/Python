from recipe_book.storage import load_recipes

def view_all_recipes():
    recipes = load_recipes()
    if not recipes:
        print("No recipes found.")
        return
    for i, recipe in enumerate(recipes, 1):
        print(f"\n{i}. {recipe['name']}")
        print("Ingredients:", ', '.join(recipe['ingredients']))
        print("Steps:", ' -> '.join(recipe['steps']))

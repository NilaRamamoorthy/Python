from recipe_data import recipes

def list_recipes():
    print("\n📖 Available Recipes:")
    for name in sorted(recipes):
        print(f"- {name}")

def view_recipe(name):
    recipe = recipes.get(name)
    if recipe:
        ingredients, steps = recipe
        print(f"\n🍽 {name}")
        print("Ingredients:")
        for item in ingredients:
            print(f"  - {item}")
        print("Steps:")
        for i, step in enumerate(steps, 1):
            print(f"  {i}. {step}")
    else:
        print("❌ Recipe not found.")

def add_recipe(name, ingredients, steps):
    if name in recipes:
        print("⚠️ Recipe already exists.")
    else:
        recipes[name] = (ingredients, steps)
        print(f"✅ Recipe '{name}' added.")

def delete_recipe(name):
    if name in recipes:
        del recipes[name]
        print(f"🗑️ Recipe '{name}' deleted.")
    else:
        print("❌ Recipe not found.")

def search_by_ingredient(ingredient):
    print(f"\n🔍 Recipes with '{ingredient}':")
    found = False
    for name, (ingredients, _) in recipes.items():
        if ingredient in ingredients:
            print(f"- {name}")
            found = True
    if not found:
        print("No recipes found.")

def get_all_categories():
    return {"Breakfast", "Lunch", "Dinner"}  # Static placeholder set

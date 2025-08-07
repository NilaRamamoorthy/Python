import json
from functools import wraps

# Decorator to log searches
def log_search(func):
    @wraps(func)
    def wrapper(self, ingredient):
        result = func(self, ingredient)
        self.search_history.append((ingredient, len(result)))
        return result
    return wrapper

class MissingIngredientError(Exception):
    pass

class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = list(ingredients)
        self.steps = list(steps)
    def __str__(self):
        ingr = "\n".join(f"- {i}" for i in self.ingredients)
        steps = "\n".join(f"{idx+1}. {s}" for idx, s in enumerate(self.steps))
        return f"{self.name}\nIngredients:\n{ingr}\nSteps:\n{steps}"

class RecipeFinder:
    def __init__(self, json_file):
        self.recipes = {}  # name → Recipe
        self.search_history = []
        self.load(json_file)

    def load(self, json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for r in data:
                self.recipes[r['name']] = Recipe(
                    r['name'], r['ingredients'], r['steps']
                )
        except FileNotFoundError:
            raise FileNotFoundError(f"Recipes file {json_file} not found")
        except KeyError as e:
            raise ValueError(f"Invalid recipe entry: missing {e}")

    @log_search
    def search_by_ingredient(self, ingredient):
        if not ingredient:
            raise ValueError("Ingredient to search must be non‑empty")
        result = []
        for recipe in self.recipes.values():
            if ingredient in recipe.ingredients:
                result.append(recipe)
        return result

    def add_recipe(self, name, ingredients, steps):
        if name in self.recipes:
            raise ValueError("Recipe already exists")
        self.recipes[name] = Recipe(name, ingredients, steps)

    def all_unique_ingredients(self):
        uniques = set()
        for recipe in self.recipes.values():
            uniques.update(recipe.ingredients)
        return uniques

    def gen_recipes(self):
        for recipe in self.recipes.values():
            yield recipe

    def show_search_history(self):
        print("Search history (ingredient, #recipes found):")
        for ingr, count in self.search_history:
            print(f"{ingr}: {count}")

# Example usage
if __name__ == "__main__":
    finder = RecipeFinder("recipes.json")

    # Search
    try:
        found = finder.search_by_ingredient("garlic")
        if not found:
            raise MissingIngredientError("No recipes with that ingredient")
        print("Found recipes with garlic:")
        for r in found:
            print(r.name)
    except MissingIngredientError as e:
        print("Error:", e)

    # Add recipe
    finder.add_recipe("Simple Salad", ["lettuce", "tomato", "olive oil"], ["Chop salad", "Drizzle oil", "Serve"])
    print("\nAll unique ingredients:", finder.all_unique_ingredients())

    print("\nAll recipes:")
    for recipe in finder.gen_recipes():
        print(recipe.name)

    print()
    finder.show_search_history()

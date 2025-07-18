# main.py

from recipe_book import add_recipe, view_recipe, list_all_utensils

# Add recipes
add_recipe(
    "Pasta",
    ["Pasta", "Salt", "Tomato Sauce", "Olive Oil"],
    ["Boil pasta", "Prepare sauce", "Mix and serve"],
    ["Pan", "Spoon", "Strainer"]
)

add_recipe(
    "Tea",
    ["Water", "Tea Leaves", "Sugar", "Milk"],
    ["Boil water", "Add tea leaves", "Add milk and sugar", "Strain and serve"],
    ["Kettle", "Cup", "Strainer"]
)

# View recipes
view_recipe("Pasta")
view_recipe("Tea")

# List all utensils used
list_all_utensils()

from recipe_book.add import add_recipe
from recipe_book.view import view_all_recipes
from recipe_book.search import search_recipe_by_name

def main():
    while True:
        print("\nRecipe Book")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. Search Recipe by Name")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            steps = input("Enter steps (separated by ';'): ").split(';')
            add_recipe(name.strip(), [i.strip() for i in ingredients], [s.strip() for s in steps])
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            name = input("Enter recipe name to search: ")
            search_recipe_by_name(name.strip())
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

from recipe_ops import list_recipes, view_recipe, add_recipe, delete_recipe, search_by_ingredient

def main():
    while True:
        print("\n🍳 Recipe Book Menu:")
        print("1. List all recipes")
        print("2. View a recipe")
        print("3. Add a new recipe")
        print("4. Delete a recipe")
        print("5. Search by ingredient")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            list_recipes()
        elif choice == '2':
            name = input("Enter recipe name: ")
            view_recipe(name)
        elif choice == '3':
            name = input("New recipe name: ")
            ingredients = input("Enter ingredients (comma separated): ").split(",")
            steps = input("Enter steps (comma separated): ").split(",")
            add_recipe(name.strip(), [i.strip() for i in ingredients], [s.strip() for s in steps])
        elif choice == '4':
            name = input("Enter recipe to delete: ")
            delete_recipe(name)
        elif choice == '5':
            ing = input("Enter ingredient to search: ")
            search_by_ingredient(ing.strip())
        elif choice == '6':
            print("👋 Exiting Recipe Book.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()

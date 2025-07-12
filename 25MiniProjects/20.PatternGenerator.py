# Pattern Generator

def star_pattern(n):
    print("\n⭐ Star Pattern:")
    for i in range(1, n+1):
        print("*" * i)

def triangle_number_pattern(n):
    print("\n🔢 Triangle Number Pattern:")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def inverted_star_pattern(n):
    print("\n🔻 Inverted Star Pattern:")
    for i in range(n, 0, -1):
        print("*" * i)

def pattern_generator():
    print("🎨 Pattern Generator")

    while True:
        try:
            size = int(input("\nEnter size of pattern (e.g., 5): "))
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    while True:
        print("\nChoose a pattern type:")
        print("1. Star Pattern")
        print("2. Number Triangle")
        print("3. Inverted Star Pattern")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ").strip()

        if choice == "1":
            star_pattern(size)
        elif choice == "2":
            triangle_number_pattern(size)
        elif choice == "3":
            inverted_star_pattern(size)
        elif choice == "4":
            print(" Exiting Pattern Generator.")
            break
        else:
            print(" Invalid choice. Try again.")

# Run the app
pattern_generator()

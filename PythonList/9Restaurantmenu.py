# Restaurant Menu System

# Initial menu: list of [dish, price]
menu = [
    ["Idly", 30],
    ["Dosa", 40],
    ["Pongal", 45]
]

# Display current menu
print("Today's Menu:")
for dish in menu:
    print(f"{dish[0]} - ₹{dish[1]}")

# Add a new dish
new_dish = ["Vada", 25]
menu.append(new_dish)
print("\nAfter adding Vada:")
for dish in menu:
    print(f"{dish[0]} - ₹{dish[1]}")

# Remove a sold-out item
sold_out = "Pongal"
menu = [dish for dish in menu if dish[0] != sold_out]
print(f"\nAfter removing sold out item '{sold_out}':")
for dish in menu:
    print(f"{dish[0]} - ₹{dish[1]}")

# Check if a dish exists
search_dish = "Dosa"
found = False
for dish in menu:
    if dish[0].lower() == search_dish.lower():
        found = True
        break
print(f"\nDish '{search_dish}' exists in menu: {found}")

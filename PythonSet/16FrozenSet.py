# Frozen sets representing meal combos (immutable)
combo1 = frozenset(["bread", "butter", "jam"])
combo2 = frozenset(["rice", "dal", "pickle"])
combo3 = frozenset(["pasta", "sauce", "cheese"])

# Dictionary to store prices for each meal combo
meal_prices = {
    combo1: 50,
    combo2: 70,
    combo3: 90
}

# Print all meal combos with their prices
print("Meal Combos and Prices:")
for combo, price in meal_prices.items():
    print(f"{set(combo)}: ₹{price}")

# Lookup a specific combo
requested_combo = frozenset(["pasta", "cheese", "sauce"])
if requested_combo in meal_prices:
    print("\nRequested combo is available.")
    print("Price:", meal_prices[requested_combo])
else:
    print("\nRequested combo is not available.")

from trip_ops import *
from suggestion_engine import suggest_destination

# Sample Usage
add_trip("Goa", ("2025-08-01", "2025-08-07"), ["Alice", "Bob"], ["Beach", "Market"])
add_trip("Manali", ("2025-09-10", "2025-09-15"), ["Charlie"], ["Snow", "Trek"])

print("All Trips:")
for i, trip in enumerate(trips):
    print(f"{i}. {trip}")

print("\nUnique Destinations:", list_unique_destinations())

print("\nSuggested Destinations:")
print(suggest_destination(["Goa"], list_unique_destinations()))

print("\nEstimated Cost for Trip 0 (₹2000/person):", calculate_cost(0, 2000))

# Movie Ticket Price Calculator
# Input: user's age
age = int(input("Enter your age: "))

# Ticket pricing logic using if-elif-else
if age < 12:
    price = 50
    category = "Child"
elif age <= 60:
    price = 120
    category = "Adult"
else:
    price = 100
    category = "Senior"

# Output
print("\n--- Ticket Summary ---")
print(f"Age Group : {category}")
print(f"Ticket Price: ₹{price}")
print("------------------------")

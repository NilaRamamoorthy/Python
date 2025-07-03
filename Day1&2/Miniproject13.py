# Profile Builder

# Step 1: Ask for name, age, and city
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Step 2: Store data in a dictionary
profile = {
    "Name": name,
    "Age": age,
    "City": city
}

# Step 3: Print formatted profile summary using f-strings
print("\n--- Profile Summary ---")
print(f"Name: {profile['Name']}")
print(f"Age : {profile['Age']}")
print(f"City: {profile['City']}")

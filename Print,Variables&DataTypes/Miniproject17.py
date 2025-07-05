# Unique Visitor Counter

# Step 1: Ask for names of people entering the shop (5 times)
visitor1 = input("Enter name of visitor 1: ")
visitor2 = input("Enter name of visitor 2: ")
visitor3 = input("Enter name of visitor 3: ")
visitor4 = input("Enter name of visitor 4: ")
visitor5 = input("Enter name of visitor 5: ")

# Step 2: Store names in a set to ensure uniqueness
unique_visitors = {visitor1, visitor2, visitor3, visitor4, visitor5}

# Step 3: Print the number of unique visitors
print(f"\nUnique visitors: {len(unique_visitors)}")

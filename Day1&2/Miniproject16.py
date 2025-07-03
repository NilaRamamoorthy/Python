# Odd/Even Number Identifier

# Step 1: Ask the user for a number
num = input("Enter a number: ")

# Step 2: Print the type before conversion
print(f"\nBefore conversion: {num} (Type: {type(num)})")

# Step 3: Convert to integer
num = int(num)

# Step 4: Check if the number is odd or even
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Step 5: Print the type after conversion
print(f"After conversion: {num} (Type: {type(num)})")

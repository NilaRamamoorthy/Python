# Simple BMI Calculator

# Step 1: Ask for weight and height
weight = input("Enter your weight in kg: ")
height = input("Enter your height in meters: ")

# Step 2: Show types before conversion
print(f"\nBefore conversion:")
print(f"Weight: {weight} (Type: {type(weight)})")
print(f"Height: {height} (Type: {type(height)})")

# Step 3: Convert to float
weight = float(weight)
height = float(height)

# Step 4: Calculate BMI
bmi = weight / (height ** 2)

# Step 5: Print BMI and type
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Type of BMI: {type(bmi)}")

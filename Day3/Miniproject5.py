# BMI Calculator & Category Checker

# Input: 
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Arithmetic: BMI formula
bmi = weight / (height ** 2)

# Category classification using if-elif
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Display results using f-string
print("\n--- BMI Report ---")
print(f"Height       : {height} m")
print(f"Weight       : {weight} kg")
print(f"BMI          : {bmi:.2f}")
print(f"Category     : {category}")
print("------------------------")

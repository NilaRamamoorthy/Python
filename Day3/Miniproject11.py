# Odd or Even Number Detector
# Input
number = int(input("Enter a number: "))

# Check using modulus operator %
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

# Display result using formatted output
print(f"\nThe number {number} is {result}.")

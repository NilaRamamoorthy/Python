# Driving License Eligibility System
# Input
age = int(input("Enter your age: "))
has_aadhar = input("Do you have an Aadhaar card? (yes/no): ").strip().lower()

eligible = False 

if age >= 18:
    if has_aadhar == "yes":  
        eligible = True
        print(" You are eligible to apply for a driving license.")
    else:
        print("You must have an Aadhaar card to apply.")
else:
    print("You must be at least 18 years old to apply.")

# Optional: Show result using logical operator
if not eligible:
    print("Access Denied.")

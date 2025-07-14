# Function to check voting eligibility
def check_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Get user input
age = int(input("Enter your age: "))
print(check_eligibility(age))

# Bonus: Lambda version
is_eligible = lambda x: "Eligible" if x >= 18 else "Not eligible"
print("Lambda Check:", is_eligible(age))

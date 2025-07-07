# 11. Voting Eligibility Checker
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"{name} is eligible to vote.")
else:
    print(f"{name} is not eligible to vote.")
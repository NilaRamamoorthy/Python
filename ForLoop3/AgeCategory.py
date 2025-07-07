#2. Age Category Classifier
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 13:
    category = "Child"
elif age <= 19:
    category = "Teen"
elif age <= 59:
    category = "Adult"
else:
    category = "Senior"
print(f"{name} is classified as: {category}")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
bmi = float(input("Enter your BMI: "))

if age > 18 and bmi < 25:
    print(f"{name} is Eligible for gym offer.")
else:
    print(f"{name} is Not Eligible.")
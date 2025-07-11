# 6. Resume Title Generator
first_name=input("Enter first name: ").strip().upper()
last_name=input("Enter last name: ").strip().upper()
role=input("Enter your role: ").strip().upper()

print("|".join([first_name,last_name,role]))
# 4. String Formatter Tool
name=input("Enter your name: ").strip().title()
salary=input("Enter salary (eg:rs3000): ").strip().lower()
new_salary=salary.replace("rs","")
new_salary=float(new_salary)
print("My name is %s and I earn ₹%.2f"%(name,new_salary))


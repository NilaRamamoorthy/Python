# Employee Management System

# Initial employee list: [Name, Department]
employees = [
    ["Alice", "HR"],
    ["Bob", "Sales"],
    ["Charlie", "Development"]
]

# Display current employees
print("Current Employees:")
for emp in employees:
    print(f"{emp[0]} - {emp[1]}")

# Add a new employee
employees.append(["Diana", "Marketing"])
print("\nAfter adding Diana:")
for emp in employees:
    print(f"{emp[0]} - {emp[1]}")

# Update department of an employee
for emp in employees:
    if emp[0] == "Charlie":
        emp[1] = "Design"
print("\n After updating Charlie's department:")
print(employees)

# Remove an employee
employees.remove(["Bob", "Sales"])
print("\nAfter removing Bob:")
print(employees)

# Sort employees alphabetically by name
employees.sort()
print("\nSorted Employee List:")
for emp in employees:
    print(f"{emp[0]} - {emp[1]}")

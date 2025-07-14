# Employee Info Manager

employees = []

def add_employee(**kwargs):
    employees.append(kwargs)
    print(f"Employee Added: {kwargs['name']} - {kwargs['role']} - ₹{kwargs['salary']}")

def show_all_employees():
    print("\n--- All Employee Records ---")
    for i, emp in enumerate(employees, 1):
        print(f"{i}. {emp['name']} | {emp['role']} | ₹{emp['salary']}")

    return employees

# Example Usage
add_employee(name="Anjali", role="Developer", salary=50000)
add_employee(name="Rahul", role="Designer", salary=45000)
add_employee(name="Meera", role="Tester", salary=40000)

employee_data = show_all_employees()

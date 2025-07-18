employees = {}

def add_employee(emp_id, name, base_salary):
    employees[emp_id] = {
        "name": name,
        "base_salary": base_salary
    }
    print(f"Employee {name} added with ID {emp_id}")

# main.py

from directory import add_employee, update_employee, remove_employee, list_employees
from search import search_by_name, search_by_department, list_departments
from utils import generate_emp_id

# Adding employees
add_employee("Alice Johnson", "HR", "Manager")
add_employee("Bob Smith", "IT", "Developer")
add_employee("Charlie Lee", "IT", "Admin")

# Updating an employee
emp_id = generate_emp_id("Bob Smith", "IT")
update_employee(emp_id, role="Senior Developer")

# Removing an employee
remove_employee(generate_emp_id("Charlie Lee", "IT"))

# Listing all employees
print("\nAll Employees:")
for emp in list_employees():
    print(emp)

# Searching
print("\nSearch by name 'Alice':")
print(search_by_name("Alice"))

print("\nEmployees in IT Department:")
print(search_by_department("IT"))

print("\nAll Departments:")
print(list_departments())

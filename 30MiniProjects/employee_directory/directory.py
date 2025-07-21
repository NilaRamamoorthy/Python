# directory.py

from typing import List, Dict, Tuple
from utils import generate_emp_id

# Global list to store employees
employees: List[Dict] = []

def add_employee(name: str, department: str, role: str):
    emp_id = generate_emp_id(name, department)
    record = {
        "id": emp_id,
        "name": name,
        "department": department,
        "role": role
    }
    employees.append(record)
    print(f"Employee {name} added.")

def update_employee(emp_id: Tuple[str, str], name: str = None, department: str = None, role: str = None):
    for emp in employees:
        if emp["id"] == emp_id:
            if name:
                emp["name"] = name
            if department:
                emp["department"] = department
            if role:
                emp["role"] = role
            print(f"Employee {emp_id} updated.")
            return
    print("Employee not found.")

def remove_employee(emp_id: Tuple[str, str]):
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print(f"Employee {emp_id} removed.")
            return
    print("Employee not found.")

def list_employees() -> List[Dict]:
    return employees

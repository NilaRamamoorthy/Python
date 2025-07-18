from payroll.employee import employees
from payroll.salary import calculate_salary
from payroll.tax import compute_tax

def generate_payslip(emp_id, bonus=0, deductions=0):
    if emp_id not in employees:
        print("Employee not found.")
        return

    emp = employees[emp_id]
    base = emp["base_salary"]
    gross = calculate_salary(base, bonus, deductions)
    tax = compute_tax(gross)
    net = gross - tax

    print("\n--- Payslip ---")
    print(f"Employee ID: {emp_id}")
    print(f"Name: {emp['name']}")
    print(f"Base Salary: ₹{base}")
    print(f"Bonus: ₹{bonus}")
    print(f"Deductions: ₹{deductions}")
    print(f"Gross Salary: ₹{gross}")
    print(f"Tax: ₹{tax}")
    print(f"Net Pay: ₹{net}")

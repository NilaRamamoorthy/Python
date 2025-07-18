from payroll.employee import add_employee
from payroll.payslip import generate_payslip

add_employee(101, "John Doe", 500000)
generate_payslip(101, bonus=20000, deductions=5000)

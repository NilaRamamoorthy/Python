import csv
from functools import wraps

# Decorator to restrict salary updates
def admin_only(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not getattr(self, 'is_admin', False):
            raise PermissionError("Admin privileges required")
        return func(self, *args, **kwargs)
    return wrapper

class NegativeValueError(Exception):
    pass

class Employee:
    def __init__(self, emp_id, name, hours, rate):
        self.emp_id = emp_id
        self.name = name
        self.hours = hours
        self.rate = rate
        self.validate()

    def validate(self):
        if self.hours < 0 or self.rate < 0:
            raise NegativeValueError("Hours and rate must be non-negative")

    def compute_salary(self):
        # Overtime pay: time-and-a-half after 40 hrs
        regular_hours = min(self.hours, 40)
        overtime_hours = max(self.hours - 40, 0)
        base = regular_hours * self.rate
        overtime = overtime_hours * self.rate * 1.5
        gross = base + overtime
        tax = self._compute_tax(gross)
        net = gross - tax
        return {'gross': gross, 'tax': tax, 'net': net}

    def _compute_tax(self, gross):
        # simple progressive tax example
        if gross <= 500:
            rate = 0.0
        elif gross <= 1000:
            rate = 0.1
        else:
            rate = 0.2
        return gross * rate

class PayrollSystem:
    def __init__(self):
        self.employees = {}   # emp_id -> Employee
        self.is_admin = False

    def add_employee(self, emp_id, name, hours, rate):
        self.employees[emp_id] = Employee(emp_id, name, hours, rate)

    @admin_only
    def update_hours(self, emp_id, hours):
        if emp_id in self.employees:
            self.employees[emp_id].hours = hours
            self.employees[emp_id].validate()
        else:
            raise KeyError("Employee not found")

    @admin_only
    def update_rate(self, emp_id, rate):
        if emp_id in self.employees:
            self.employees[emp_id].rate = rate
            self.employees[emp_id].validate()
        else:
            raise KeyError("Employee not found")

    def generate_payslips(self, filename='payslips.csv'):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Hours', 'Rate', 'Gross', 'Tax', 'Net'])
            for emp in self.employees.values():
                sal = emp.compute_salary()
                writer.writerow([emp.emp_id, emp.name, emp.hours, emp.rate,
                                 f"{sal['gross']:.2f}",
                                 f"{sal['tax']:.2f}",
                                 f"{sal['net']:.2f}"])

    def overtime_employees(self):
        for emp in self.employees.values():
            if emp.hours > 40:
                yield emp

    def run_all(self, filename='payslips.csv'):
        print("Generating payslips and reporting overtime:")
        self.generate_payslips(filename)
        for emp in self.overtime_employees():
            print(f"Overtime: {emp.name} worked {emp.hours}h")

# Example usage
if __name__ == "__main__":
    payroll = PayrollSystem()
    payroll.add_employee('E001', 'Alice', 38, 25)
    payroll.add_employee('E002', 'Bob', 45, 20)
    payroll.is_admin = True
    payroll.update_hours('E001', 42)
    payroll.update_rate('E002', 22)
    payroll.run_all('payslips.csv')

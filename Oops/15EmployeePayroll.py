# Employee Payroll System

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id})"

    @staticmethod
    def calculate_tax(amount):
        tax = 0.1 * amount if amount > 5000 else 0.05 * amount
        return tax


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Payroll:
    def __init__(self):
        self.records = []

    def add_employee(self, emp):
        self.records.append(emp)

    def process_payroll(self):
        print("\nPayroll Summary:")
        for emp in self.records:
            salary = emp.calculate_salary()
            tax = Employee.calculate_tax(salary)
            net_salary = salary - tax
            print(f"{emp} => Gross: ₹{salary}, Tax: ₹{tax}, Net: ₹{net_salary}")


# ----------------------
# 📌 Sample Usage
# ----------------------

if __name__ == "__main__":
    # Create employees
    emp1 = FullTimeEmployee("Kiran", "FT101", 6000)
    emp2 = PartTimeEmployee("Rahul", "PT205", 200, 20)

    # Add to payroll system
    payroll = Payroll()
    payroll.add_employee(emp1)
    payroll.add_employee(emp2)

    # Process payroll
    payroll.process_payroll()

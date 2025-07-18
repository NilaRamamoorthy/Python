def compute_tax(salary):
    if salary <= 250000:
        return 0
    elif salary <= 500000:
        return salary * 0.05
    elif salary <= 1000000:
        return salary * 0.2
    else:
        return salary * 0.3

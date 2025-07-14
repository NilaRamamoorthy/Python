# EMI = [P x R x (1+R)^N] / [(1+R)^N – 1]
# P = Principal, R = Monthly Interest Rate, N = Number of Months

def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return round(emi, 2)

# Bonus using lambda (for single-line EMI calculator)
emi_lambda = lambda p, r, y: round(
    (p * (r/1200) * ((1 + (r/1200)) ** (y*12))) / (((1 + (r/1200)) ** (y*12)) - 1), 2
)

# Example Usage
p = 500000  # principal
r = 7.5     # annual interest rate
t = 10      # tenure in years

print("EMI using function:", calculate_emi(p, r, t))
print("EMI using lambda :", emi_lambda(p, r, t))

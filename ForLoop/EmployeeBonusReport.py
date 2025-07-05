employees = [("Asha", 92), ("Ravi", 80), ("Nila", 60)]

for name, score in employees:
    if score >= 90:
        bonus = 10000
        remark = "Excellent"
    elif score >= 75:
        bonus = 5000
        remark = "Good"
    else:
        bonus = 2000
        remark = "Needs Improvement"

    print(f"{name}: {remark} - ₹{bonus}")

# 8. Attendance Counter
attendance = [input(f"Day {i+1} (P/A): ").upper() for i in range(7)]
present = attendance.count('P')
if present >= 5:
    print("Eligible for exam")
else:
    print("Not eligible")
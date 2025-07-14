
# 13. Employee Shift Scheduler
shifts = [
    (101, 'John', ('09:00', '17:00')),
    (102, 'Alice', ('10:00', '18:00')),
    (103, 'Bob', ('08:00', '16:00'))
]
for emp_id, name, (start, end) in shifts[:5]:
    print(f"{name}: {start} to {end}")

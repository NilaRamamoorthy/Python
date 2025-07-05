marks = [int(input(f"Enter mark {i+1}: ")) for i in range(5)]
total = sum(marks)
percentage = total / 5

if any(m < 35 for m in marks):
    result = "Fail"
else:
    if percentage >= 75:
        result = "Distinction"
    elif percentage >= 60:
        result = "First Division"
    elif percentage >= 50:
        result = "Second Division"
    else:
        result = "Pass"

print(f"\nTotal: {total}, Percentage: {percentage:.2f}%, Result: {result}")
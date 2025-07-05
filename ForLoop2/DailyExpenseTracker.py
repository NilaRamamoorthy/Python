expenses = [float(input(f"Enter expense for day {i+1}: ")) for i in range(7)]
total = sum(expenses)
print(f"Total weekly expense: ₹{total}")
if total > 3000:
    print("Cut down on expenses.")
items = [float(input("Enter item price: ")) for _ in range(5)]
friends = int(input("Enter number of friends: "))
total = sum(items)
split = total / friends
print(f"Each person should pay: ₹{split:.2f}")
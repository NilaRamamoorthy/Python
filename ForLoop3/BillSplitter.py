# 9. Bill Splitter Between Friends
total = float(input("Enter total bill: "))
friends = int(input("Enter number of friends: "))
if friends >= 1:
    print(f"Each pays: ₹{total/friends:.2f}")
else:
    print("Number of friends must be at least 1")
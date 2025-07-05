price = float(input("Enter product price: "))
if price >= 2000:
    final = price * 0.8
elif price > 1000:
    final = price * 0.9
else:
    final = price
print(f"Final Price after discount: ₹{final:.2f}")

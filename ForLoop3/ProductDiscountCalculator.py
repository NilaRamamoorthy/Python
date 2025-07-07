# 10. Online Product Discount Calculator
price = float(input("Enter product price: "))
if price >= 2000:
    discount = 0.3
elif price >= 1000:
    discount = 0.1
else:
    discount = 0
final = price * (1 - discount)
print(f"Final price after discount: ₹{final:.2f}")
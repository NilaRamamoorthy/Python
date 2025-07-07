# 14. Product Search Tool
products = ["pen", "notebook", "eraser", "bag"]
search = input("Enter product name: ").lower()
if search in products:
    print("Available")
else:
    print("Out of stock")
products = ["Pen", "Book", "Mouse", "Laptop"]
search = input("Enter product name to search: ")

for item in products:
    if item.lower() == search.lower():
        print("Product Found")
        break
else:
    print("Not Found")

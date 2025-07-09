#14. Shopping Cart Input App
cart=[]
while True:
    items=input("Enter item to add to cart: ").lower()
    if items=="":
        continue
    if items=="done":
        break
    cart.append(items)
    
else:
    #This will work only when the loop is completed successfuly without break which is not possible in this case
    for item in cart:
        print(item)
print("Your shopping cart: ")
for item in cart:
        print(item)
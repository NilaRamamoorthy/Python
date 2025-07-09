food=[]
total=0
while True:
    items=input("Enter food item to add: ").lower()
    if items=="done":
        break
    food.append(items)
    total+=1

print(food)
print(f"Total number of items in the list: {total}")

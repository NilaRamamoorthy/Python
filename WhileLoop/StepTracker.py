#17. Step Tracker
days=1
total=0
while days<=7:
    steps=int(input("Enter Steps: "))
    if steps==0:
        continue
    total+=steps
    days+=1
else:
    average=int(total/7)
    print(f"Total steps in a week: {total}")
    print(f"Average Steps in a week: {average}")

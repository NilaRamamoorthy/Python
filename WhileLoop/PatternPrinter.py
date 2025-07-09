#12. Pattern Printer
number=int(input("Enter a number: "))
star=1
while star<=number:
    star2=1
    while star2<=star:
       print("*", end=" ")
       star2+=1
    print()   
    star+=1
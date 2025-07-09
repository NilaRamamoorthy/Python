#15. Even Number Skipper
num=1
while num<=20:
    if num%2==0:
        num+=1
        continue
    print(num)
    num+=1
    
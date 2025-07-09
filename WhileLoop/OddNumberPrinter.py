#3. Odd Number Printer
number=1
list_num=[]
while number<21:
    if number%2==0:
        number+=1
        continue

    list_num.append(number)
    number+=1
print(list_num)
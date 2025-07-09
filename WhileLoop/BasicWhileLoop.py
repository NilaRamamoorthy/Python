#Task 1
num=0
print("Numbers from 1 to 10")
while num<10:
    num+=1
    print(num)
print("-"*40)

#Task 2
num2=1
print("Even numbers from 2 to 20")
while num2<21:
    if num2%2==0:
        print(num2)
    num2+=1
print("-"*40)

#Task 3
num3=10
print("Reverse numbers from 10 to 1")
while num3>=1:
    print(num3)
    num3-=1
print("-"*40)

#Task 4
num4=int(input("Enter a number: "))
number=1
while number<=num4:
    print(number)
    number+=1
print("-"*40)

#Task 5
num5=1
total=0
while num5<51:
    total+=num5
    num5+=1
print(f"Sum Of Numbers from 1 to 50: {total}")
print("-"*40)

#Task 6
num6=int(input("Enter nmber for Factorial: "))
fact=1
number1=num6
while num6>=1:
    fact*=num6
    num6-=1
print(f"Factorial of {number1} is {fact}")
print("-"*40)

#Task 7
num7=3
while num7<31:
    if num7%3==0:
        print(num7)
    num7+=1
print("-"*40)

#Task 8
while True:
    user_input=input("Enter 'stop' if you want to stop: ").lower()
    if user_input=="stop":
        break
print("-"*40)


#Task 9
num8=100
while num8>49:
    print(num8)
    num8-=5
print("-"*40)


#Task 10
user_list=[]
num9=1
print("Enter list items:")
while num9<6:
    user_input=input(f"Enter Number {num9}:")
    user_list.append(user_input)
    num9+=1
print(user_list)




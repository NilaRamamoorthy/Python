# Functions with Parameters and Return Values (11–15)

# Task 11: Define a function divide(a, b) and return the quotient. Handle divide-by-zero.
def divide(a,b):
    if b==0:
        print("Anything divisible by 0 is 0")
    return a/b
result=divide(30,5)
print(f"The division result is: {result}")
print("-"*40)

# Task 12: Create a function full_name(fname, lname) that returns a full name.
def full_name(fname,lname):
    return fname+" "+lname
fname=input("Enter first name: ").strip().title()
lname=input("Enter last name: ").strip().title()
result=full_name(fname,lname)
print(f"Your Full Name: {result}")
print("-"*40)

# Task 13: Write a function that takes age as input and returns if the user is eligible to vote.
def eligible(age):
    if age>=18:
        return "You are eligible to vote"
    return "You are underage and not eligible to vote"
age=int(input("Enter Your Age: "))
result=eligible(age)
print(result)
print("-"*40)

# Task 14: Create a function calc_discount(price, discount_percent) that returns the final price.
def calc_discount(price,discount_percent):
    discount=price*discount_percent/100
    total=price-discount
    return total
result=calc_discount(10000,20)
print(f"Total amount to pay: {result}")
print("-"*40)

# Task 15: Write a function to calculate and return the average of 3 numbers.
numbers=[34,45,56]
def avg(numbers):
    avg=int(sum(numbers)/3)
    return avg
result=avg(numbers)
print(f"The average of 3 numbers is: {result}")
print("-"*40)

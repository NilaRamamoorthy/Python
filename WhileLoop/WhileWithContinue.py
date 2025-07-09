#While with continue Statement (16–25)
#Task 16
num=1
while num<21:
    if num %2==0:
        continue
    print(num)
    num+=1
print("-"*40)

#Task 17
entry=1
while entry<6:
    get_number=int(input("Enter a number: "))
    if get_number<0:
        continue
    else:
        entry+=1
print("-"*40)

# Task 18:
n = 1
while n <= 10:
    if n == 5:
        n += 1
        continue
    print(n)
    n += 1
print("-"*40)

# Task 19: 
n = 1
while n <= 20:
    if n % 3 == 0:
        n += 1
        continue
    print(n)
    n += 1
print("-"*40)

# Task 20:
words = []
count = 0
while count < 10:
    word = input("Enter a word: ")
    if len(word) < 3:
        continue
    words.append(word)
    count += 1
print("Words collected:", words)
print("-"*40)

# Task 21: 
s = "python programming"
i = 0
while i < len(s):
    if s[i].lower() not in 'aeiou':
        i += 1
        continue
    print(s[i], end=" ")
    i += 1
print("-"*40)

# Task 22: 
num = 1
count = 0
while num <= 100:
    if num % 2 == 0:
        num += 1
        continue
    count += 1
    num += 1
print("\nOdd numbers between 1 and 100:", count)
print("-"*40)

# Task 23: 
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    if num % 5 != 0:
        continue
    print(f"{num} is a multiple of 5")
print("-"*40)

# Task 24:
n = 1
while n <= 30:
    if n % 2 == 0 and n % 3 == 0:
        n += 1
        continue
    print(n)
    n += 1
print("-"*40)

# Task 25:
n = 1
while n <= 20:
    if n % 2 == 0:
        n += 1
        continue
    print(f"Cube of {n} is {n**3}")
    n += 1
print("-"*40)

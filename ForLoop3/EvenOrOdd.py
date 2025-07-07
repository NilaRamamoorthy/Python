# 7. Even/Odd Number Classifier
numbers = [int(input("Enter number: ")) for _ in range(10)]
for n in numbers:
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")
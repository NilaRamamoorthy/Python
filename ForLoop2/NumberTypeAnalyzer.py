numbers = [int(input("Enter a number: ")) for _ in range(5)]
for n in numbers:
    print(f"{n} is", end=" ")
    if n % 2 == 0:
        print("Even", end=", ")
    else:
        print("Odd", end=", ")
    if n >= 0:
        print("Positive")
    else:
        print("Negative")
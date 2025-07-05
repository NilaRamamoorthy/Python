marks = [int(input("Enter mark: ")) for _ in range(5)]
for m in marks:
    if m >= 90:
        print(f"{m} - A")
    elif m >= 75:
        print(f"{m} - B")
    elif m >= 50:
        print(f"{m} - C")
    else:
        print(f"{m} - D")
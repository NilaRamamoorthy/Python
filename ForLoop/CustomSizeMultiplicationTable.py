size = int(input("Enter table size (e.g. 5): "))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()

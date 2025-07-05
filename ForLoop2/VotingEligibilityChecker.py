ages = [int(input("Enter age: ")) for _ in range(5)]
for a in ages:
    if a >= 18:
        print(f"Age {a}: Eligible to vote")
    else:
        print(f"Age {a}: Not eligible")
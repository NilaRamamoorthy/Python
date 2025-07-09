#18. Voting Eligibility Checker
people=1
count=0
while people<6:
    age=int(input("Enter your age: "))
    people+=1
    if age>=18:
        count=+1
    
print(f"Number of eligible voters: {count}")
#10. User Info Collector
user_info={}
count=0
while count<5:
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    if name=="" or age<=0:
        print("Enter valid info.")
        continue
    email=input("Enter email: ")
    if email:
        pass
    user_info[name]=age
    count+=1

print("Collected User Info:\n")
for k,v in user_info.items():
    print(f"{k} - {v} years old")

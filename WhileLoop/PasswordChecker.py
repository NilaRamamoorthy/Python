# 2. Password Checker with Limited Attempts
attempt=1
password="1234"
while attempt<4:
    enter_passwd=input("Enter Password: ")
    attempt+=1
    if enter_passwd==password:
        print("Correct Password!")
        break
       
else:
    print("Too many attempts!")
     
     
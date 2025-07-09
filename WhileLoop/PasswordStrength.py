#7. Password Strength Tester
while True:
    passwd=input("Enter password of min 6 characters: ")
    passwd_len=len(passwd)
    if passwd_len<6:
        continue
    else:
        print("Password Accepted.")
        break
    
        
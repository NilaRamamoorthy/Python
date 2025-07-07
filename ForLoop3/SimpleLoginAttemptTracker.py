#4. Simple Login Attempt Tracker
username = "admin"
password = "1234"
for i in range(3):
    u = input("Enter username: ")
    p = input("Enter password: ")
    if u == username and p == password:
        print("Login Successful")
        break
else:
    print("Account Locked")
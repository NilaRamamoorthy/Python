# 5. Secure Password Masker

password=input("Enter your password: ").strip()
length=len(password)-2
masked=password[0]+"*"*length+password[-1]
print(f"Masked password: {masked}")
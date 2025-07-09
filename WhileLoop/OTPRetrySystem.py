#20. OTP Retry System
otp="1234"
attempt=1
while attempt<4:
    user_entry=input("Enter OTP: ").strip()
    attempt+=1
    if user_entry==otp:
        print("OTP is correct")


else:
    print("OTP failed")
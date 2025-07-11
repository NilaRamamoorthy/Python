import random
import string
phone_no=input("Enter your phone number: ").strip()
otp=phone_no[-4:-2]+random.choice(string.ascii_upper)+phone_no[-2:-1]+random.choice(string.ascii_upper)+phone_no[-1:]
print(f"Your OTP is: {otp}")
# 17. Email Validator
email = input("Enter your email: ").strip()

# Basic structure check
if "@" in email and "." in email:
    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index+1:]

    if len(username) > 5 and domain == "gmail.com":
        print("Valid Gmail ID")
    else:
        if len(username) <= 5:
            print(" Username must be more than 5 characters.")
        if domain != "gmail.com":
            print(" Email must be from 'gmail.com'.")
else:
    print("Invalid email format. Must contain '@' and '.'")


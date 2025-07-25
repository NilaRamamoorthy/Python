import re

def email_sender(emails):
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    count = 0
    total = len(emails)
    for email in emails:
        if not pattern.match(email):
            continue
        received = yield email  # send requests batch size override
        count += 1
        if received:  # received is desired batch size
            # simulate consuming more if requested
            while count < received and count < total:
                yield emails[count]
                count += 1
    return f"Sent {count} emails in total"

# Usage:
emails = ["user1@example.com", "bad@", "user2@site.org", "user3@domain", "user4@test.net"]
gen = email_sender(emails)
try:
    print("Email:", next(gen))
    print("Email:", next(gen))
    print("Request extended batch size:", gen.send(3))  # ask for 3 returns?
    # Simulate failure:
    gen.throw(ValueError("SMTP failure"))
except ValueError as e:
    print("Caught error:", e)
except StopIteration as e:
    print("Completed:", e.value)

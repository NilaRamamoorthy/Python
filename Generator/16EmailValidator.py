import re

# Email regex matching standard format
pattern = re.compile(r'^\S+@\S+\.\S+$')

def valid_email_generator(emails, limit=10):
    """Generator expression yielding only valid emails up to limit."""
    return (email for email in emails if pattern.fullmatch(email))

# Usage demo:
emails_list = [
    "a@example.com", "bad@", "user2@site.org", "nope.com",
    "person@domain.net", "invalid@", "ok@ok.com", "test@x.co",
    "hello@world.io", "foo@bar.com", "last@good.org", "extra@skip.me"
]

gen = valid_email_generator(emails_list)
print("Valid emails (up to 10):")
count = 0
for email in gen:
    print(email)
    count += 1
    if count >= 10:
        break

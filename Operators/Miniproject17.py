# Basic Chat Filter App
# Predefined list of banned words
banned_words = ["bad", "hate", "stupid", "idiot", "ugly"]

# Get user input message
message = input("Enter your message: ").lower()

# Check if any banned word is in the message
found = False
for word in banned_words:
    if word in message:
        found = True
        break

# Output
if found:
    print(" Message blocked: Inappropriate language detected.")
else:
    print(" Message accepted.")

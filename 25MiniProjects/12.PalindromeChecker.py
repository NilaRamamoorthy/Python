# Palindrome Checker

# Function to check if a word/sentence is a palindrome
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Main loop
def palindrome_checker():
    print("Palindrome Checker")
    while True:
        user_input = input("Enter a word or sentence (or type 'exit' to stop): ").strip()
        if user_input.lower() == "exit":
            print("👋 Exiting Palindrome Checker.")
            break
        if is_palindrome(user_input):
            print("It's a palindrome!")
        else:
            print("Not a palindrome.")

# Run the app
palindrome_checker()

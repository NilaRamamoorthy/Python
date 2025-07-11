# SECTION 5: Concatenation and Repetition (36–40)

# 36 Concatenate first name and last name with a space in between.
firstname=input("Enter first name: ").title()
lastname=input("Enter last name: ").title()
fullname=f"{firstname} {lastname}"
print(f"Your Full name: {fullname}")
print("-"*40)

# 37 Write a program that asks for a name and prints it 3 times using *.
name=input("Enter name: ").title()
print((name+" ")*3)
print("-"*40)

# 38 Create a sentence by joining five different words using +.
word1 = "Learning"
word2 = "Python"
word3 = "is"
word4 = "fun"
word5 = "everyday!"

sentence = word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5
print(sentence)
print("-"*40)

# 39 Use .join() to combine a list of characters into a word.
chars = ['H', 'e', 'l', 'l', 'o']
word = ''.join(chars)
print(word)
print("-"*40)

# 40 Take user input for a name and print “Welcome <name>” using string concatenation.
name = input("Enter your name: ").strip()
welcome_message = "Welcome " + name
print(welcome_message)
print("-"*40)
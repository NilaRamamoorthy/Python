secret_num=8
attempt=1
while attempt<6:
    guess=int(input("Guess the number: "))
    attempt+=1
    if guess==secret_num:
        print("You guessed the right number")
        break
   
else:
    print("Sorry! You have'nt guessed the number in 5 tries")
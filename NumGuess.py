
low=0
high=100
guess=int((low+high)/2)
print("Please think of a number between 0 and 100!")
print("Is your secret number", guess)
userinput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while userinput != "c":
    if userinput == "h":
        high = guess
        guess = int((low+high)/2)
        print("Is your secret number", guess)
        userinput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    elif userinput == "l":
        low = guess
        guess = int((low + high) / 2)
        print("Is your secret number", guess)
        userinput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    else:
        print("Sorry, I did not understand your input")
        print("Is your secret number", guess)
        userinput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over.", "Your secret number was:", guess)








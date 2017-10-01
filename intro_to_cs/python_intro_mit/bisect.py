print("Please think of a number between 0 and 100!")
guessed = False
lowbound = 0
highbound = 100

while guessed == False:
    response = (lowbound + highbound) // 2
    print("Is your secret number " + str(response) + "?")
    hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if hint == "l":
        lowbound = response
    elif hint == "h":
        highbound = response
    elif hint == "c":
        print("Game over. Your secret number was: " + str(response))
        guessed = True
    else:
        print("Sorry, I did not understand your input.")

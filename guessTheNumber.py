n = 69
G = 8
while True:
    print("You have %d guesses. " % G)
    INP = int(input("Enter a number: "))
    G = G - 1
    if G == 0:
        print("Game Over\nYou Lose!")

        break
    if INP == 69:
        print("\ncongratulations you have successfully guessed the number")
        print("\n No. of guesses taken to guess the number %d ." % (8 - G))
        print("\n No, of guesses left %d" % G)
        break
    elif INP < 69:
        print("\n Increase the value of input")
    else:
        print("\n Decrease the value of input")
    continue

print("Welcome to the Wall Game, guess the ")
def wallscript():
    userinput = raw_input("Letter: ")
    if userinput == "c":
        print("well done you guessed the letter!!!")
    elif userinput == "C":
         print("well done you guessed the letter!!!")
    else:
        print("You are wrong!")
        wallscript()
wallscript()

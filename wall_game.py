print("wecome to the wall game, guess the ")
def wallscript():
    userinput = raw_input("Letter: ")
    if userinput == "c":
        print("well done you guessed the letter!!!")
    elif userinput == "C":
         print("well done you guessed the letter!!!")
    else:
        print("you are wrong")
        wallscript()
wallscript()

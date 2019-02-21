import random

def dice():
    diceRoll = random.randint(1,6)
    diceRolled = str(diceRoll)
    print("Your dice roll is " + diceRolled + ".")

def question():
    quest = input("Would you like to roll again? Press y or n. ")
    if quest[0] == "y":
        dice()
        return question()
    elif quest[0] == "n":
        return
    else:
        print("Invalid Input, please try again.")
        return question()

dice()
question()
exitApp = input("Press any key to Exit.")

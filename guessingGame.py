import random
number=int(input("Enter a number from 1 to 9"))
guess=random.randint(0,9)
chance=0
while chance < 5:
    guess1=int(input("Enter your guess"))

    if (guess == number):
        print("Congratulations you won")
        chance=chance+1
    else:
        print("You lost", "try again")
        print("Used chance ", chance)
    chance=chance+1


    
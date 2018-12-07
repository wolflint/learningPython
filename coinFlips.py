# import required modules
import random, cmd, sys

# input number validation
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except:
            print("Not an interger! Try again.")
            continue
        else:
            return userInput

def tossCoins (amount):
    heads = 0
    tails = 0
    for i in range(amount):
        # generate variable value 0 or 1 randomly
        toss = random.randint(0, 1)
            # if variable value is 0, display HEADS
        if toss == 0:
            print("HEADS\n")
            heads+=1
        # else if variable value is 1, display TAILS
        elif toss == 1:
            print("TAILS\n")
            tails+=1
    return [heads, tails]

# user input
amount = inputNumber("Please enter the amount of times you'd like to flip the coin: ")
results = tossCoins(amount)
print("Heads: " + str(results[0]) + " Tails: " + str(results[1]))
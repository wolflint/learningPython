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
            break

# user input
multiple = inputNumber("Please enter the amount of times you'd like to flip the coin: ")

# user input validation
# while inputNumber not in range(0, 99):
#     print("Invalid input. Please type in a number between 1 and 99")
#     inputNumber = int(input("How many times should the coin be flipped? "))
# check if multiplier argument has any input data
if multiple > 0:
    for value in range(0, multiple):
        # generate variable value 0 or 1 randomly
        toss = random.randint(0, 1)

        # if variable value is 0, display HEADS
        if toss == 0:
            print("HEADS")
        # else if variable value is 1, display TAILS
        elif toss == 1:
            print("TAILS")

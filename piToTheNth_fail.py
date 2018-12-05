#import requirements
import math, decimal

# value of pi
pi = 3.14159265358979323846264338327950288419716939937510

# defining round down function
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

# user input validation for interger
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except:
            print("I need an interger! Try again...")
            continue
        else:
            return userInput
            break

# prompt for user input and store in variable
piLength = inputNumber("To which decimal place should Pi be displayed? ")

# check that piLength is within range
while piLength not in range(-1, 51):
    print("Error. You've selected a number out of range.\nPlease choose a number between 0 and 50")
    piLength = inputNumber("To which decimal place should Pi be displayed? ")

decimal.getcontext().prec = (piLength + 2)
print(decimal.Decimal(pi))

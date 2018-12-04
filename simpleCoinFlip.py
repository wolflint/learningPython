# import the random library
import random

# generate variable value 0 or 1 randomly
toss = random.randint(0, 1)

# if variable value is 0, display HEADS
if toss == 0:
    print("HEADS")
# else if variable value is 1, display TAILS
elif toss == 1:
    print("TAILS")

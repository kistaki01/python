from consolServices import *
from gameService import *
import random

lowernum:int =inBetween(0,9)
biggernum:int = inBetween(40,50)

randomnum:int = random.randint(lowernum,biggernum)

guesses:int = guessCounter(randomnum)

print(f"{guesses} probalkozasbol talalta el")

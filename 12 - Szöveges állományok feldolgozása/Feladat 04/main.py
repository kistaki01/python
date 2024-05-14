from typing import *
from lottery import *
from fileService import *
from lotteryService import *

guesses:List[Lottery] = getGuessesFromFile("adatok.txt")

writeGuessesToFile(guesses)


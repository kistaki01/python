from consoleServices import *
from mathServices import *
from gameService import *

lowNum:int = getIntNumberBetweenInterval("kerem az elso szamot:",0,9)
bigNum:int = getIntNumberBetweenInterval("kerem a nagyobb erteket",40,50)
rnd:int = randomNum(lowNum,bigNum)
guesses:int = guessCounter(f"talalja ki {lowNum} es {bigNum} kozotti szamot:",rnd)

print(f"{guesses} probalkozasbol talalta ki a szamot")








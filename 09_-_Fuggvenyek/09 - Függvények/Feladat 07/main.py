from consoleServices import *
from paintService import *

wall:int = getIntNumber("adja meg a fal meretet:")
cans :int = paintCalculator(wall)
price:int = priceCalculator(cans)

print(f"ekkor a fal: {wall}, ennyi festek kell: {cans} ennyit kell fizetni: {price}")
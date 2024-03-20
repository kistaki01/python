from consoleServices import *
from paintService import *

wall = getIntNumber("adja meg a fal meretet:")
cans = paintCalculator(wall)
price = priceCalculator(cans)

print(f"ekkor a fal: {wall}, ennyi festek kell: {cans} ennyit kell fizetni: {price}")
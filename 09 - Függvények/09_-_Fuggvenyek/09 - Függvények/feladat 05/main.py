from workCalculator import *
from consoleServices import *

name = getName("kerme a nevet  ")
wage = workHours()
Whours = getIntNumberBetweenInterval("kerem a dolgozott orakat",0,77)

print(f"ennyi orat dolgozott: {Whours}, ennyi fizetest kap: {wage}, a neve: {name}")
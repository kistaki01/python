from workCalculator import *
from consoleServices import *

name = getString("kerem a nevet:")
wHours = getIntNumberBetweenInterval("kerem a dolgozott orakat",0,77)
wage = getWage(wHours)

print(f"ennyi orat dolgozott: {wHours}, ennyi fizetest kap: {wage}, a neve: {name} ")
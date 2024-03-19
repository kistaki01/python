from consoleServices import *
from gradeService import *

point = getIntNumberBetweenInterval("kerem a szamot",0,100)
grade = gradeCalc(point)

print(f"ennyi lett a pontszama: {point}, Ez lett a jegye: {grade}")
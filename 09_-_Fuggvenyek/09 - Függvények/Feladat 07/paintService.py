from consoleServices import *
import math

def paintCalculator(wall:int) -> int:
    paintAmount = wall * 0.15
    cans : int = 0
    if(paintAmount % 1 == 0):
       cans = paintAmount * 1 
    else:
       cans = math.ceil(paintAmount)
    return cans

def priceCalculator(cans:int) -> int:
    price: int = 0
    price = cans * 980
    return price
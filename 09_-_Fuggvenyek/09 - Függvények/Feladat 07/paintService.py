from consoleServices import *
import math

def paintCalculator(wall:int, price: float = 0.15) -> int:
    paintAmount = wall * price
    cans : int = 0
    if(paintAmount % 1 == 0):
       cans = paintAmount * 1 
    else:
       cans = math.ceil(paintAmount)
    return cans

def priceCalculator(cans:int, price:int = 980) -> int:
    return cans * price
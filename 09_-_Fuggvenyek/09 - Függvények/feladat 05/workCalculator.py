from consoleServices import *

def getWage(wHours:int) -> int:
    overWork :int = 0
    wage:int = 0 
    hourlyRate : int = 1000  
    baseHours : int = 40 
    if(wHours >= baseHours):
       overWork = wHours - baseHours
       wage = (baseHours * hourlyRate) + (overWork * (hourlyRate * 1.5))
    elif(wHours == 0):
        print("nem kapott fizetest")
    else:
        wage = wHours * hourlyRate
    
    return wage


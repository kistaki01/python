from consoleServices import *

def getWage(promt:str) -> int:
    overWork :int = 0
    while(Whours == None or (Whours > 77 or Whours < 0)):
        Whours = getIntNumber("kerem a szamot")               
        if(Whours > 40):
            overWork = Whours - 40
            baseWage = Whours - overWork
            wage = overWork * 1500 and baseWage * 1000
        elif(Whours == 0):
            print("nem kapott fizetest")
        else:
            baseWage * 1000



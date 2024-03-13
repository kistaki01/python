from consoleServices import *

def guessCounter(promt:str,rnd:int) -> int:
    guesses:int = 0
    data:str = ""
    num:int = None
    while(num == None or num != rnd):
       num = getIntNumber("kerem a szamot:")
    if(num > rnd):
        print("a szam nagyobb mint a keresendo szam")
        
    else:
        print("kisebb a szam mint  a keresendo szam")
         
        guesses += 1
    
    return guesses
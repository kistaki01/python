from consoleServices import getIntNumber

def guessCounter(randomNum) -> int:
    guesses:int = 0
    num:int = None

    while(num == None or (num != randomNum)):
        num = getIntNumber("kerem a szamot:")
        if(num > randomNum):
            print("a szam nagyobb mint a kitalalando szam")
        else:
            print("a szam kisebb mint a kitalalando szam")
        guesses += 1
    
    return  guesses
    
    
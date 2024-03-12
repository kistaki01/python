import consoleServices

def guessCounter(promt:str,rnd:int) -> int:
    guesses:int = 0
    data:str = ""
    num:int = None
    while(num == None or num != rnd):
        data = input("kerem a szamot:")
        isNumber: bool = data.replace("-", "", 1).isdigit()
        if(isNumber):
            num = int(data)
            if(isNumber and num > rnd):
                print("nagyobb a beirt szam mint a random")
            else:
                print("kisebb a beirt szam mint random")
        else:
            print("\nNem szamot adott meg!")
         
        guesses += 1
    return guesses
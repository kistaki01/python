def getIntNumber () -> int:
    number: int = None
    data: str = ""

    while(number == None or number < 0 or number > 9):
        print("kérem a számot: ", end="")
        data=input()
    
        isNumber : bool = data.replace("-", "", 1).isdigit()
        if(isNumber):
            number = int(data)

        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number

def getFloatNumber () -> float:
    number : float = None
    data : str = "" 

    while(number == None):
        print("kérem a számot: ", end="")
        data=input()
        
        isNumber : bool = data.replace("-", "", 1).replace(",","", 1).replace(".","", 1).isdigit()
        if(isNumber):
            number = float(data.replace(",","."))

        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number
            
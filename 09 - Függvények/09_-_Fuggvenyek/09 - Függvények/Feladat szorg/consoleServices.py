import time
import os


def getIntNumber (promt: str) -> int:
    number: int = None
    data: str = ""
    while(number == None):

        print("promt, ", end=": ")
        data=input()
    

        isNumber : bool = data.replace("-", "", 1).isdigit()

        if(isNumber):
            number = int(data)


        elif(not isNumber):

            print("\nNem szamot adott meg!")

            time.sleep(2)

            os.system("cls")

    return number

def getFloatNumber (promt: str) -> float:
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
            
def getIntNumberLessThen (promt: str, max: int) -> int:
    number: int = None
    data: str = ""

    while(number == None or number > max):
        print("promt, ", end=": ")
        data=input()
    
        isNumber : bool = data.replace("-", "", 1).isdigit()

        if(isNumber):
            number = int(data)
            if(number > max):
                print(f"a meg adott zsam nem lehet nagyobb mint {max}")
                time.sleep(1)
                os.system("cls")
        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number

def getIntNumberGreaterThen (promt: str, min: int) -> int:
    number: int = None
    data: str = ""

    while(number == None or number < min):
        print("promt, ", end=": ")
        data=input()
    
        isNumber : bool = data.replace("-", "", 1).isdigit()

        if(isNumber):
            number = int(data)
            if(number < min):
                print(f"a meg adott zsam nem lehet kisebb mint {min}")
                time.sleep(1)
                os.system("cls")
        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number
            
def getIntNumberBetweenIntervals (promt: str, min: int, max:int) -> int:
    number: int = None
    data: str = ""

    while(number == None or number < min or number > max):
        print(f"{promt}, [{min},{max}] ", end=": ")
        data=input()
    
        isNumber : bool = data.replace("-", "", 1).isdigit()

        if(isNumber):
            number = int(data)
            if(number < min or number > max):
                print(f"a zsam nem a megadott tartomany ban van")
                time.sleep(1)
                os.system("cls")
        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number 


def getLetter(promt: str)-> str:
    letter : str = ""
    isLetter: bool = False

    while(letter == "" or not isLetter):

        print(promt, end="")
        letter = input()
        
        isLetter = len(letter) == 1 and letter.isalpha()

        
        if(not isLetter):
            print("\nszam/mas van benne!")
            time.sleep(3)
            os.system("cls")
    return letter


def getSpecificLetter(promt: str, goodLetters: list[str])-> str:
    letter : str = ""
    isLetter: bool = False

    while(letter == "" or not isLetter):

        print(promt, end="")
        letter = input()
        
        isLetter = len(letter) == 1 and letter.isalpha() and (letter in goodLetters)

        
        if(not isLetter):
            print("\nszam/mas van benne!")
            time.sleep(3)
            os.system("cls")
    return letter
            
            
    
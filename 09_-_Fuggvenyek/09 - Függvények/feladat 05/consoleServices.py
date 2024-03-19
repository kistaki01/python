import os
import time

def getIntNumber(promt: str) -> int:
    number: int = None
    data:str = ""

    while(number == None):
        print(promt, end=": ")
        data = input()
        
        isNumber: bool = data.replace("-", "", 1).isdigit()
        
        if(isNumber):
            number = int(data)
        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number

def getIntNumberLessThen(promt: str, max: int) -> int:
    number: int = None
    data:str = ""

    while(number == None or number > max):
        print(promt, end=": ")
        data = input()
        
        isNumber: bool = data.replace("-", "", 1).isdigit()
        
        if(isNumber):
            number = int(data)
        if(isNumber and number > max):
            print(f"\nA megadott szam nem lehet nagyobb mint {max}!")
            time.sleep(2)
            os.system("cls")
        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number

def getIntNumberGreaterThen(promt: str, min: int) -> int:
    number: int = None
    data:str = ""

    while(number == None or number < min):
        print(promt, end=": ")
        data = input()
        
        isNumber: bool = data.replace("-", "", 1).isdigit()
        
        if(isNumber):
            number = int(data)
        if(isNumber and number < min):
            print(f"\nA megadott szam nem lehet kisebb mint {min}!")
            time.sleep(2)
            os.system("cls")
        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number

def getIntNumberBetweenInterval(promt: str, min: int, max: int) -> int:
    number: int = None
    data:str = ""

    while(number == None or number < min or number > max):
        print(f"{promt} [{min}, {max}]", end=": ")
        data = input()
        
        isNumber: bool = data.replace("-", "", 1).isdigit()
        
        if(isNumber):
            number = int(data)
        if(isNumber and (number < min  or number > max)):
            print(f"\nA megadott szam nincs az intervallumban!")
            time.sleep(2)
            os.system("cls")
        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number

def getFloatNumber(promt: str) -> float:
    number:float = None
    data:str = ""

    while(number == None):
        print(promt, end=": ")
        data = input()
        
        isNumber: bool = data.replace("-", "", 1).replace(",", "", 1).replace(".", "", 1).isdigit()
        
        if(isNumber):
            number = float(data.replace(",", "."))
        elif(not isNumber):
            print("\nNem szamot adott meg!")

            time.sleep(2)
            os.system("cls")
    
    return number

def getLetter(promt: str) -> str:
    letter:str = None
    isLetter: bool = False

    while(letter == None or not isLetter):
        print(promt, end=": ")
        letter = input()

        isLetter = len(letter) == 1 and letter.isalpha()

        if(not isLetter):
            print("Nem betut adott meg!")
            time.sleep(2)
            os.system("cls")
    
    return letter

def getSpecificLetter(promt: str, goodLetters: list[str]) -> str:
    letter:str = None
    isLetter: bool = False

    while(letter == None or not isLetter):
        print(promt, end=": ")
        letter = input()

        isLetter = len(letter) == 1 and letter.isalpha() and (letter in goodLetters)

        if(not isLetter):
            print("Nem betut adott meg!")
            time.sleep(2)
            os.system("cls")
    
    return letter
def getName() -> str:
    name=None
    data:str=""

    while (name == None or len(name) <2 or not name.isalpha()):
        print("Adja meg a nevet: ")
        name = input()

        areAllLettersInString = name.isalpha
    
    if(areAllLettersInString and len(name)<2):
        print("lealabb 2 karakternek kell lennie")

    if(not areAllLettersInString):
        print("A nevben csak betuk lehetnek")
    os.system("cls")
    return name

def getString(promt: str) -> str:
    letter:str = None
    isLetter: bool = False

    while(letter == None or not isLetter):
        print(promt, end=": ")
        letter = input()

        isLetter = len(letter) >= 2 and letter.isalpha()

        if(not isLetter):
            print("nem nevet adott meg")
            time.sleep(2)
            os.system("cls")
    
    return letter
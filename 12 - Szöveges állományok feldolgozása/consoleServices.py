import os
import time

def getIntNumber(prompt: str) -> int:
    number: int = None
    data:str = ""

    while(number == None):
        print(prompt, end=": ")
        data = input()
        
        isNumber: bool = data.replace("-", "", 1).isdigit()
        
        if(isNumber):
            number = int(data)
        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number

def getIntNumberLessThen(prompt: str, max: int) -> int:
    number: int = None
    data:str = ""

    while(number == None or number > max):
        print(prompt, end=": ")
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

def getIntNumberGreaterThen(prompt: str, min: int) -> int:
    number: int = None
    data:str = ""

    while(number == None or number < min):
        print(prompt, end=": ")
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

def getIntNumberBetweenInterval(prompt: str, min: int, max: int) -> int:
    number: int = None
    data:str = ""

    while(number == None or number < min or number > max):
        print(f"{prompt} [{min}, {max}]", end=": ")
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

def getFloatNumber(prompt: str) -> float:
    number:float = None
    data:str = ""

    while(number == None):
        print(prompt, end=": ")
        data = input()
        
        isNumber: bool = data.replace("-", "", 1).replace(",", "", 1).replace(".", "", 1).isdigit()
        
        if(isNumber):
            number = float(data.replace(",", "."))
        elif(not isNumber):
            print("\nNem szamot adott meg!")

            time.sleep(2)
            os.system("cls")
    
    return number

def getLetter(prompt: str) -> str:
    letter:str = None
    isLetter: bool = False

    while(letter == None or not isLetter):
        print(prompt, end=": ")
        letter = input()

        isLetter = len(letter) == 1 and letter.isalpha()

        if(not isLetter):
            print("Nem betut adott meg!")
            time.sleep(2)
            os.system("cls")
    
    return letter

def getSpecificLetter(prompt: str, goodLetters: list[str]) -> str:
    letter:str = None
    isLetter: bool = False

    while(letter == None or not isLetter):
        print(prompt, end=": ")
        letter = input()

        isLetter = len(letter) == 1 and letter.isalpha() and (letter in goodLetters)

        if(not isLetter):
            print("Nem betut adott meg!")
            time.sleep(2)
            os.system("cls")
    
    return letter

def getSpecificString(prompt: str, goodString: list[str]) -> str:
    string: str = None
    isString: bool = False

    while(string == None or not isString):
        print(prompt, end=": ")
        string = input()

        isString = string.isalpha and (string in goodString)

        if(not isString):
            print("Nem stringet adott meg!")
            time.sleep(2)
            os.system("cls")

    return string
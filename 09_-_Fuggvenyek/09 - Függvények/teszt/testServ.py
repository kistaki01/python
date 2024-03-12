import os
import time

def getNumber(inputNumber: int, numberType: int) -> str:
    number: int = None
    data: str = ""
    while (number == None):
        print("kérem a számot: ", end="")
        data = inputNumber
        isNumber = data.replace("-", "", 1).replace(",", "", 1).replace(".", "", 1).isdigit()

        if(isNumber):
            number = numberType(data.replace(",", "."))

        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(2)
            os.system("cls")

    return number

def getIntNumber() -> int:
    return getNumber

def getFloatNumber() -> float:
    return getNumber
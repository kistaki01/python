from typing import *
import time
import os



def getDecision(prompt: str) -> int:
    num: int = None
    data: str = ""

    while(num == None):
        print(prompt, end="\n dontes:  ")
        data=input()
        isNumber : bool = data.replace("-", "", 1).isdigit()

        if(isNumber):
            number = int(data)
        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(3)
            os.system("cls")
    return number
    







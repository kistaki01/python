import time
import os
import random
rnd:int = random.randint(0,9)
tries:int = 5
guessed:bool = False
number:int = None
data:str=""
while(tries > 0 and not guessed):
    while(number == None or (number<0 or number>9)):
        data = input("kerem a szamot:")
        isNumber: bool = data.replace("-","",1).isdigit()
        if(not isNumber):
            number = int(data)
        if(isNumber and (number < 0 or number > 9)):
            print("\n a szam nem a kert tartomanyban van")
            time.sleep(3)
            os.system("cls")
        elif(not isNumber):
            print("\n Nem szamot adott meg")
            time.sleep(3)
            os.system("cls")
    tries = tries - 1
    if(number == rnd and tries >= 0):
      guessed = True
if(guessed == True and tries >= 5):
    print("eltalalta a szamot")

import os
import time
import random
number:str = None
data:str = ""
rnd:int = random.randint(0,9)
tries:int = 5
guessed:bool = False

while(tries > 0 and not guessed):
    while((number == None or (number<0 or number>9)) and tries > 0):
        print("kerem a szamot:")
        data = input()
        isNumber: bool = data.replace("-","",1).isdigit()
        if(isNumber):
            number = int(data)
            if(not isNumber and (number < 0 or number > 9)):
                print("\n a szam nem a kert tartomanyban van")
                time.sleep(3)
                os.system("cls")
        else:
            print("\n Nem szamot adott meg")
            time.sleep(3)
            os.system("cls")
    
        if(number==rnd):
            guessed==True
            time.sleep(3)
            os.system("cls")
            print("eltalalta a szamot")
        else:
            tries -= 1
            number = None
            print(f"meg {tries} probalkozasod van")
            if(tries == 0):
                print("elfogyott a probalkozas")

        
import os
import time
number:int = None
data:str = "" 
interest:int = 0
months:int = 0
while(number == None or (number < 0 or number >= 100000)):
    data = input("kerem a szamot:")
    isNumber: bool = data.replace("-","",1).isdigit()
    if(isNumber):
        number = int(data)
        if(isNumber and (number < 0 or number >= 100000)):
            print("\n a szam nem a kert tartomanyban van")
            time.sleep(3)
            os.system("cls")
    else:
        print("\n Nem szamot adott meg")
        time.sleep(3)
        os.system("cls")

while(number < 100000):
    interest = number * 0.02
    number += interest
    months += 1

print(f"ennyi honap alatt erte el: {months}")
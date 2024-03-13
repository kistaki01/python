import os
import time
number:int = None
data:str = "" 
minus:bool = False
plus:bool = False


while(number == None or (number<99 or number>999 and  number > -99 or number <-999)):
    data = input("kerem a szamot:")
    isNumber: bool = data.replace("-","",1).isdigit()
    if(isNumber):
        number = int(data)
        if((number <= 99 or number > 999)):
            print("\n a szam nem a kert tartomanyban van")
            time.sleep(3)
            os.system("cls")
    elif(not isNumber):
        print("\n Nem szamot adott meg")
        time.sleep(3)
        os.system("cls")

if(number > 99):
    plus = True
else:
    minus = True

if(number % 7 == 0 and (plus == True and minus == False) or (plus == False and minus == True)):
    print("a szam oszthato hettel")
else:
    print("a szam nem oszthato hettel")
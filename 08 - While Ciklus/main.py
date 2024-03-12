import os 
import time
data:str = ""
number:int = None

while(number == None or(number < 0 or number > 9)):
    data = input("kerem a szamot")
    isNumber:bool = data.replace("","-").isdigit()
    if(isNumber):
        number = int(data)
        if(isNumber and (number < 0 or number > 9)):
            print(" a szam nem amegadott tartomanyban van ")
    else:
        print("nem szam")
        time.sleep(3)
        os.system("cls")
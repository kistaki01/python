import os
import time
number:int = None
data:str = "" 
age:str = ""
while(number == None or (number < 0 or number > 99)):
    
    data = input("kerem a szamot:")
    isNumber: bool = data.replace("-","",1).isdigit()
    if(isNumber):
        number = int(data)
        if((number < 0 or number > 99)):
            print("\n a szam nem a kert tartomanyban van")
            time.sleep(3)
            os.system("cls")
    else:
        print("\n Nem szamot adott meg")
        time.sleep(3)
        os.system("cls")

if(number >= 0 and number <= 6):
    age = "gyermek"
elif(number > 6 and number <= 18):
    age = "iskolas"
elif(number > 18 and number <= 65):
    age = "dolgozo"
else:
    age = "nyugdijas"

print(f"az illeto a {age} korosztalyba esik")
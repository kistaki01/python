import os
import time
serialnum:int = None
data:str = ""
drunkensailor:str =""
print("a valasztaho uditok:\n kola: 1 \n sprite: 2 \n canadaDry: 3 \n DrPepper: 4 \n vodkanarancs: 5")


while(serialnum == None or (serialnum < 0 or serialnum>6)):
   
    data = input("kerem a szamot:")

    isNumber: bool = data.replace("-","",1).isdigit()
    if(isNumber):
        serialnum = int(data)
    if(isNumber and (serialnum < 0 or serialnum > 6)):
        print("\n a szam nem a kert tartomanyban van")
        time.sleep(3)
        os.system("cls")
      
    elif(not isNumber):
        print("\n Nem szamot adott meg")
        time.sleep(3)
        os.system("cls")

match(serialnum):
    case 1:
        drunkensailor = "kola/cola"
    case 2:
        drunkensailor = "sprite"
    case 3:
        drunkensailor = "canadaDry"
    case 4:
        drunkensailor = "DrPepper"
    case 5:
        drunkensailor = "vodka narancs/igazsagszerum"

print(f"a kert udito: {drunkensailor}") 
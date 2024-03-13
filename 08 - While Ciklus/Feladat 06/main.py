import time
import os
sum:int = 0
tries:int = 0
number:int = None
data:str = ""
while(sum < 100):
    while(number == None):
        data = input("kerem a szamot:")
        isNumber: bool = data.replace("-","",1).isdigit()
        if(isNumber):
            number = int(data)
        elif(not isNumber):
            print("\n Nem szamot adott meg")
            time.sleep(3)
            os.system("cls")
    
    sum += number
    tries += 1
        
    print(f"a szam eddigi osszege: {sum}")
    print(f"eddig ennyi probalkozas volt: {tries}")
    
    number = None
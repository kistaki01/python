import time
import os
sum:int = 0
tries:int = 0
number:int = None
data:str = ""
border:int = None
while(border == None or (border < 100)):
    data = input("kerem a hatarerteket:")
    isborder: bool = data.replace("-","",1).isdigit()
    if(isborder):
        border = int(data)
    elif(not isborder):
        print("\n Nem szamot adott meg")
        time.sleep(3)
        os.system("cls")

while(sum < border):
    while(number == None):
        data = input("kerem a szamot:")
        isNumber: bool = data.replace("-","",1).isdigit()
        if(isNumber):
            number = int(data)
        else:
            print("\n Nem szamot adott meg")
            time.sleep(3)
            os.system("cls")
    
    sum += number
    tries += 1
        
    print(f"a szam eddigi osszege: {sum}")
    number = None

print(f"eddig ennyi probalkozas volt: {tries}")
    
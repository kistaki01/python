import os
import time 

snumber: int = None
bnumber:int = None
data:str = ""
reverse:int = None 
while(snumber == None):
    data = input("kerem az elso szamot:")
    issNumber: bool = data.replace("-","").isdigit()
    if(issNumber):
        snumber = int(data)
    else:
        print("\nNem szamot adott meg!")
        time.sleep(3)
        os.system("cls")

while(bnumber == None or (bnumber <= snumber)):
    data = input("kerem a masodik szamot:")
    isbNumber: bool = data.replace("-","").isdigit()
    if(isbNumber):
        bnumber = int(data)
        if(bnumber <= snumber):
            print("\nNem megfeleo tartomanyban van a masodik szam!")
            time.sleep(3)
            os.system("cls")
    else:
        print("nem szamott adott meg")

while(reverse == None or (bnumber - snumber) < reverse):
    data = input("kerem a leptek erteket:")
    isreverse: bool = data.replace("-","").isdigit()
    if(isreverse):
        reverse = int(data)
        if(((bnumber - snumber) < reverse)):
            print("\nNem megfelelo szamot adott meg!")
            time.sleep(3)
            os.system("cls")
    else:
        print("nem szamott adott meg")

for i in range(bnumber, snumber-1,-reverse):
    print(i)
import os
import time
import random
even:int = None
data:str = "" 
odd:int = None
rndnum:int = None
exam:bool = False
fourdiv:int = 0
while(even == None or (even % 2 != 0)):
    data = input("kerem a paros szamot:")
    isNumber: bool = data.replace("-","",1).isdigit()
    if(isNumber):
        even = int(data)
        if(isNumber and (even % 2 != 0)):
            print("\n a szam nem a kert tartomanyban van")
            time.sleep(3)
            os.system("cls")
    else:
        print("\n Nem szamot adott meg")
        time.sleep(3)
        os.system("cls")


while(odd == None or (odd < even) and (odd % 2 == 0)):
    data = input("kerem a paratlan szamot:")
    isnumber: bool = data.replace("-","",1).isdigit()
    if(isNumber):
        odd = int(data)
        if(isNumber and (odd % 2 == 0)):
            print("\n a szam nem a kert tartomanyban van")
            time.sleep(3)
        os.system("cls")
    else:
        print("\n Nem szamot adott meg")
        time.sleep(3)
        os.system("cls")

rndnum:int = random.randint(even,odd)
print(f"a random szam : {rndnum}")

if(rndnum - even > odd - rndnum):
    print(f"a paratlan szam van kozelebb a {rndnum} szamhoz")
else:
    print(f"a paros szam van kozelebb a {rndnum} szamhoz")

avarage = (even + odd) / 2 

for i in range(even,odd,1): 
    if(i % 4 == 0):
        fourdiv += 1
    

print(f"a szamok atlaga {avarage}")
print(f"a 4-el oszthato szamok: {fourdiv}")
      




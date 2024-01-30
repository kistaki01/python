import os
import time 

number: int = None
data:str = "" 
while((number == None) or (0 > number or number > 9)):
    data = input("kerem a szamot:")
    isNumber: bool = data.replace("-","").isdigit()
    if(isNumber):
        number = int(data)
    elif(isNumber and (0 > number or number > 9)):
        print("\nA szam nem a megadott tartomanyban van")
    else:
        print("\nNem szamot adott meg!")

        time.sleep(3)

        os.system("cls")

print(f"a beolvasott szam {number}")
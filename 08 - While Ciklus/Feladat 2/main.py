import os
import time 

number: float = None
data:str = ""

while((number == None) or (0 > number or number > 9)):

    data = input("kerem a szamot:")
    if(data.replace("-","").replace(".","").isdigit()):
        number = float(data)
    else:
        print("\nNem szamot adott meg!")
        time.sleep(3)
        os.system("cls")

print(f"a beolvasott szam {number}")
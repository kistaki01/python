import os
import time 

name:str = None
data:str = ""

while((name == None)):
    print("kerem a nevet:")
    data = input()
    isName:bool = data.isalpha()
    if(isName):
        name = str(data)
    if(isName and len(name)<=1):
        print("\n nem nevet adott meg")
        time.sleep(3)
        os.system("cls")
    elif(not isName):
        print("\nNem nevet adott meg")
        time.sleep(3)
        os.system("cls")

print(f"a nev: {name}") 
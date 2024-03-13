import os
import time 

name:str = None
while((name == None)):
    print("kerem a nevet:")
    name = input()
    isName:bool = name.isalpha()
    if(isName and len(name)<=1):
        print("\n nem nevet adott meg")
        time .sleep(3)
        os.system("cls")
        
    elif(not isName):
        print("\nNem nevet adott meg")
        time.sleep(3)
        os.system("cls")
    else:
        break

print(f"a nev: {name}")
#areAlllettersinstring: bool = false
#while(name==None or len(name) < 2 or not name.alpha()):
    #print("kerem adja meg a nevet")
    #name = input

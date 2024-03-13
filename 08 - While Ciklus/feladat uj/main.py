import os
import time
number:int = None
max:int = None
data:str = "" 
while(number == None or (number != 0)):
    data = input("kerem a szamot:")
    isNumber: bool = data.replace("-","",1).isdigit()
    
    if(isNumber):
        number = int(data)
    else:
        print("nem szamot adott meg")
    
    if(max == None):
       max = number
    elif(number > max):
        max = number
print(f"a legnagyobb szam az: {max}")
            
      

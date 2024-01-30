import os
import time 

number: int = None
number2:int = None
data:str = "" 
while(number == None):
    data = input("kerem az elso szamot:")
    isNumber: bool = data.replace("-","").isdigit()
    if(isNumber):
        number = int(data)
    else:
        print("\nNem szamot adott meg!")
        time.sleep(3)
        os.system("cls")

while(number2 == None):
    data = input("kerem a masodik szamot:")
    isNumber2: bool = data.replace("-","").isdigit()
    if(isNumber2):
        number2 = int(data)
        if(isNumber2 and (number2 <= number)):
            print("\nNem megfelelo szamot adott meg!")
            time.sleep(3)
            os.system("cls")

for i in range(number2, number-1,-1):
    print(i)


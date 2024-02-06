import os
import time 

n: int = None
data:str = "" 
elevens:int = 0
sum:int = 0

while((n == None) or ( 0 > n or n > 99)):
    data = input("kerem a szamot:")
    isn: bool = data.replace("-","").isdigit()
    if(isn):
        n = int(data)
        if(isn and (0 > n or n > 99)):
            print("\nA szam nem a megadott tartomanyban van")
    else:
        print("\nNem szamot adott meg!")

        time.sleep(3)

        os.system("cls")

for i in range(0,n+1,2):
    print(i)

for j in range(0,n+1,1):
    if(j % 5 == 0):
        sum += j

print(f"5tel oszthato szamok osszege: {sum}")

for k in range(0,n+1,1):
    if(k % 11 == 0 and k != 0):
        elevens += 1

print(f"{elevens} szam oszthato 11el az {n} szamban ")

for l in range(0,n+1,1):
    if(l % 7 == 3):
        print(l)
        


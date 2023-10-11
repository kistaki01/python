print("adjon meg egy szamot:", end="")
number: int = int(input())

if(number > 0):
    print(f"{number} nagyobb 0-tol")

elif(number < 0):
    print(f"{number} kisebb 0-tol")
    
else:
    print(f"a beirt szam 0")
    
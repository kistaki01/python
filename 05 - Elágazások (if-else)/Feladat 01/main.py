print("adjon meg egy szamot:", end="")
number:int = int(input)

if(number>0):
    print(f"{number} nagyobb 0-nal")
elif(number < 0):
    print(f"{number} kisebb 0-tol")
else:
    print(f"a beirt szam nulla")

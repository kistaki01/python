print("adjon meg egy szamot:", end="")
number: int = int(input())

if(number > 0 and number <=9):
    print(f"{number} egyjegyű szám")
elif(number >=10 and number <= 999):
    print(f"{number} kétjegyű szám"):
elif(number >=100 and number <= 999):
    print(f"{number} háromjegyű szám")
else:
    print(f"{number} nagyobb 99-nél, vagy kiesbb 0-nál")
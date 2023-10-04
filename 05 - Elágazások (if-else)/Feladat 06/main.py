print("adjon meg egy szamot:", end="")
number:int = int(input())

print("adjon meg egy számot", end="")
number2:int = int(input())

print("adjon meg egy szamot:", end="")
number3:int = int(input())

if(number < number2 < number3):
    print(f"{number} \n {number2} \n {number3}")
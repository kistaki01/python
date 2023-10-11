
print("Adjon meg egy szamot:", end="")
number: int = int(input())

print("Adjon meg még egy szamot:", end="")
number2: int = int(input())

print("Adjon meg egy harmadik szamot:", end="")
number3: int = int(input())

if(number > number3 and number > number2):
    if(number2 > number3):
        print(f"{number}")
    


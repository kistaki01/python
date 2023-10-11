print("Adjon meg egy szamot:", end="")
number: int = int(input())

print("Adjon meg még egy szamot:", end="")
number2: int = int(input())

if(number < number2):
    print(f"{number2} nagyobb mint {number}")
elif(number > number2):
    print(f"{number} nagyobb mint {number2}")
else:
    print(f"{number} és {number2} egyenlo")


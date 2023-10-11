
print("Adjon meg egy szamot:", end="")
number: int = int(input())

print("Adjon meg még egy szamot:", end="")
number2: int = int(input())

if(number < number2):
    print(f"{number}, {number2}")

elif(number > number2):
    print(f"{number2}, {number}")

else:
    print("A két szám egyenlo")



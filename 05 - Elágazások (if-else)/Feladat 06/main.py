<<<<<<< HEAD
print("Adjon meg egy szamot:", end="")
number: int = int(input())

print("Adjon meg még egy szamot:", end="")
number2: int = int(input())

print("Adjon meg egy harmadik szamot:", end="")
number3: int = int(input())

if(number < number2 and number2 < number3):
    print(f"{number}, {number2}, {number3}")

elif(number < number2 and number2 > number3 and number < number3):
    print(f"{number}, {number3}, {number2}")

elif(number > number2 and number2 < number3 and number < number3):
    print(f"{number2}, {number}, {number3}")

elif(number < number2 and number2 < number3 and number > number3):
    print(f"{number2}, {number3}, {number}")

elif(number < number2 and number2 > number3 and number > number3):
    print(f"{number3}, {number2}, {number}")

else:
    print(f"{number3}, {number}, {number2}")
=======
print("adjon meg egy szamot:", end="")
number:int = int(input())

print("adjon meg egy számot", end="")
number2:int = int(input())

print("adjon meg egy szamot:", end="")
number3:int = int(input())

if(number < number2 < number3):
    print(f"{number} \n {number2} \n {number3}")
>>>>>>> d8f21474fac6d6ed5bf87f625655fe6e1f5c9f9e

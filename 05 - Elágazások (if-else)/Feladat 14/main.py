print("Adjon meg egy szamot:", end="")
x: int = int(input())

print("Adjon meg egy szamot:", end="")
y: int = int(input())

print("Adjon meg egy szamot:", end="")
z: int = int(input())

div1: bool = x % y == 0
div2: bool = x % z == 0

if  (div1 and div2) :
    print(f"{x} oszthato {y} es {z}")
elif (div1) :
    print(f"{x} oszthato {y} de nem {z}")
elif (div2) :
    print(f"{x} oszthato {z} de nem {y}")
else:
    print(f"{x} nem oszthato sem {y} sem {z}")
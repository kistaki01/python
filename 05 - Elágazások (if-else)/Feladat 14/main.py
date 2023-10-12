print("Adjon meg egy szamot:", end="")
x: int = int(input())

print("Adjon meg még egy szamot:", end="")
y: int = int(input())

print("Adjon meg egy harmadik szamot:", end="")
z: int = int(input())

divisible1: bool = x % y == 0
divisible2: bool = x % z == 0

if  (divisible1 and divisible2) :
    print(f"{x} oszthato {y} es {z}")
elif (divisible1) :
    print(f"{x} oszthato {y} de nem {z}")
elif (divisible2) :
    print(f"{x} oszthato {z} de nem {y}")
else:
    print(f"{x} nem oszthato sem {y} sem {z}")
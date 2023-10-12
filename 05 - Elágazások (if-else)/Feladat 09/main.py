print("adjon meg egy szamot:", end="")
x: int = int(input())

print("adjon meg egy masodik szamot:", end="")
y: int = int(input())

if (x % y == 0):
    print(f"{y} osztoja {x}-nek.")
else:
    print(f"{y} nem osztoja {x}-nek.")
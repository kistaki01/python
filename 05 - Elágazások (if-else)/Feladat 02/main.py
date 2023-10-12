print("adjon meg egy szamot:", end="")

number: int = int(input())

if(number >= 0):
    print(f"A {number} pozitiv")
else:
    print(f"A {number} negativ")

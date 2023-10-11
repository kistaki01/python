print("adjon meg egy szamot:", end="")
number: int = int(input())

if (number % 4 == 0 and number % 6 == 0):
    print(f"{number} osztható 4-gyel és 6-tal is.")
    
else:
    print(f"{number} nem osztható 4-gyel és 6-tal is.")
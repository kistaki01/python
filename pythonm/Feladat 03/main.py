print("Adjon meg egy szamot:", end="")
number: int = int(input())

if(number > -30 and number < 40):
    print(f"{number} -30 és 40 kozott van")

else:
    print(f"{number} nincs -30 es 40 kozott")
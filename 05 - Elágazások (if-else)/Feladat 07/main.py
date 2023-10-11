print("Adjon meg egy szamot:", end="")
number: int = int(input())

if( number % 5  == 0):
    print(f"{number} oszthato 5-tel")
else:
    print(f"{number} nem osztahto 5-tel")
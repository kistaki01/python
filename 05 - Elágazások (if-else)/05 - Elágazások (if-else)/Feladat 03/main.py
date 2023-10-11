print("adjon meg egy szamot:", end="")
number:int = int(input())

if(number > -30 and number < 40):
    print(f"a {number} -30 és 40 között található")
else:
    print(f"a {number} nincs -30 és 40 között")

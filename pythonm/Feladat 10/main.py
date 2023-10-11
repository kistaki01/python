print("adjon meg egy szamot:", end="")
number: int = int(input())

if (number % 2 == 0 and number % 3 == 0):
    print("ZIZI")

elif (number % 2 == 0):
    print("BIZ")

elif (number % 3 == 0):
    print("BAZ")

else:
    print("a szam nem oszthato sem 2-vel sem 3-mal")
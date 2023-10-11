print("adjon meg egy szamot:", end="")
number: int = int(input())

if (number % 2 == 0):
    print("a szam paros")

else:
    print("a szam paratlan")


if (number > 0):
    print("a szam pozitiv")

elif (number < 0):
    print("a szam negativ")

else:
    print("a szam nulla")


if (number % 5 == 0):
    print("a szam oszthato 5-tel")

else:
    print("a szam nem oszthato 5-tel")
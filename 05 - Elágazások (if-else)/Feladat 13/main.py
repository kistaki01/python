print("adjon meg egy szamot:", end="")
number: int = int(input())

if (0 <= number and number <= 9):
    print("egyjegyu a szam.")

elif (10 <= number and number <= 99):
    print("ketegyu a szam.")
    
elif (100 <= number and number <= 999):
    print("haromegyu a szam")

else:
    print("a szam vagy tobb mint haromjegyu vagy negativ")
print("adjon meg egy szamot:", end="")
number: int = int(input())

if(number > 20 and number < 20):
    print(f"a {number} 10 és 20 között található")
elif(number < -10 and number > -20):
    print(f"a {number}-10 és -20")
else:
    print(f"{number} nincsen 10 és 20 között. nincsen -10 és -20 között")

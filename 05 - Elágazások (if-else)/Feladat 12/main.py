print("adjon meg egy szamot:", end="")
number: int = int(input())


if (10 <= number and number <= 20):
    print(f"{number} 10 es 20 kozott van")

elif (-20 <= number and number <= -10):
    print(f"{number} -10 es -20 kozott van")
else:
    print(f"{number} nincsen se -10 és -20 se 10 es 20 kozott")


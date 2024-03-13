print("hany soros legyen a piramis: ", end="")

row = int(input())

for i in range(1, row + 1, 2):
    for m in range((row - i) //2 ):
        print("\t", end="")

    for b in range(1, i + 1, 1):
        print(b, end='\t')

    print()
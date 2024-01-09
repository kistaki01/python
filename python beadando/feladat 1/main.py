print("hany soros legyen a piramis: ", end="")

row = int(input())

for i in range(0, row, 1):
    for m in range(0, i+1, 1):
        print(m+1, end=" ")
    
    print("\t")
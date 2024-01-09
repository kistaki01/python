print("hany soros legyen a piramis: ", end="")

row = int(input())

for i in range(row, 0, -1):
   for m in range(i, 0, -1):
       print(m, end=" ")
    
   print("\t")
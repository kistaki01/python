print("adja meg a kezdo erteket: ", end="")
sValue = int(input())

print("adja meg a veg erteket: ", end="")
eValue = int(input())

if(sValue % 2 == 0):
    sValue += 1

for i in range(sValue, eValue+1, 2):
    print(i)



print("adja meg a kezdo erteket: ", end="")
sValue = int(input())

print("adja meg a vegso erteket: ", end="")
eValue = int(input())

if(eValue % 2 == 1):
    eValue -= 1

for i in range(eValue, sValue-1,-2):
    print(i)
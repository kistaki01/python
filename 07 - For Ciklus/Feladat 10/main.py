sValue : int = None
eValue :int = None
sum : int = 0
product : int = 1

print("kérem adja meg a kezdo erteket: ", end="")
sValue = int(input())

print("kérem adja meg a vegso erteket: ", end="")
eValue = int(input())

for i in range(sValue, eValue+1,1):
    sum += i
    product *= i

print(f"osszeadas:{sum}")
print(f"szorzas:{product}")

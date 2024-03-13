even:int = 0
odd:int = 0

print("adja meg a kezdoerteket: ", end="")
startValue = int(input())

print("adja meg a vegerteket: ", end="")
endValue = int(input())

for i in range(startValue, endValue+1,1):
    if(startValue % 2 == 0):
        even += i
    else:
        odd += i

if(even > odd):
    print("parosbol van tobb")
elif(even < odd):
    print("paratlanbol van tobb")
else:
    print("egyenloek")
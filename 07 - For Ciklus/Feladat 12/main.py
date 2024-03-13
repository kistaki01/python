counter = 0

print("adja meg a kezdoerteket: ", end="")
startValue = int(input())

print("adja meg a vegerteket: ", end="")
endValue = int(input())

if(startValue % 3 == 1):
    startValue +=2
elif(startValue % 3 == 2):
    startValue += 1
elif(startValue == 0):
    startValue += 3

for i in range(startValue,endValue+1,3):
    counter += 1

print(f"3al oszthato szamok osszege {counter}")

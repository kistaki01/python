seven:int = 0
five:int = 0
print("adja meg a kezdoerteket: ", end="")
startValue = int(input())

print("adja meg a vegerteket: ", end="")
endValue = int(input())

for i in range(startValue, endValue+1,1):
    if(i % 7 == 0 and i % 5 == 0):
        seven += i
        five += i
    elif(i % 5 == 0):
        five += i
    elif(i % 7 == 0):
        seven += i
    
if(five > seven):
    print("ottel tobb az oszthato")
elif(five < seven):
    print("tobb a hettel oszthato")
elif(five == seven):
    print("egyenlo a ketto")
else:
    print("nem oszthato se 5el se hettel")

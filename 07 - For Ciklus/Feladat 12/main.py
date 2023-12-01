print("adja meg a kezdoerteket: ", end="")
startValue = int(input())

print("adja meg a vegerteket: ", end="")
endValue = int(input())

summary: int = 0
product: int = 1

for i in range(startValue, endValue + 1, 1):
    if( i % 2 == 0):
        summary += i
    else:
        product = product * i

print(f"osszege: {summary}")
print(f"szorata: {product}")
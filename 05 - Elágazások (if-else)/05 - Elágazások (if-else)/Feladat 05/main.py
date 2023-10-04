print("adjon meg egy szamot:", end="")
number:int = int(input())
print("adjon meg egy számot", end="")
number2:int = int(input())
if(number < number2):
    print(f"{number} \n {number2}")
else:
    print(f"{number2} \n {number}")
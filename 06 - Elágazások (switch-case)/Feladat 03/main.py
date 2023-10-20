selectDrink: int = None
output: str = None
Error: str = None

print("1 - Cola Coca")
print("2 - Cola Pepsi")
print("3 - Cola Fanta")
print("4 - Sprite")

print("Kerem az udito sorszamat: ", end="")
selectDrink = int(input())

match(selectDrink):
    case 1:
        output = "Coca Cola"
    case 2:
        output = "Pepsi"
    case 3: 
        output = "Fanta"
    case 4:
        output = "Sprite"
    case _:
        Error = "nem letezo"

if(Error == None and selectDrink >= 1 and selectDrink <= 4):
    print(f"on {output} valasztott")
elif(Error != None):
    print(output)

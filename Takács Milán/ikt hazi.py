
selectFood4: int = None
selectFood1: int = None
selectFood2: int= None
selectFood3: int= None
output: str = None
output2: str = None
output3: str = None
output4: str = None
Error: str = None

print("eloetelek:")
print("zöldségleves - 1")
print("husleves - 2")
print("gyumolcsleves - 3")
print("nem kerek eloetelt - 0")
print(f"kerem valasszon egy eloetelt ha akar: ", end="")
selectFood1 = int(input())
match(selectFood1):
    case 1:
        output = "zoldsegleves"
    case 2:
        output = "husleves"
    case 3:
        output = "gyumolcsleves"
    case 0:
        output = "nem kerek eloetelt"
    case _:
        Error = "nincs ilyen a listan"

print("foetelek:")
print("sultcsirkecomb - 4")
print("sult csirkemell - 5")
print("rakottzoldseg - 6")
print("spagetti - 7")
print("pizza - 8")
print("nem kerek foetelt - 0")
print(f"kerem valasszon egy foeteleket ha akar: ", end="")
selectFood2 = int(input())
match(selectFood2):
    case 4:
        output2 = "sultcsirkecomb"
    case 5:
        output2 = "sult csirkemell"
    case 6:
        output2 = "rakottzoldseg"
    case 7:
        output2 = "spagetti"
    case 8:
        output2 = "pizza"
    case 0:
        output2 = "nem kerek foetelt"
    case _:
        Error = "nincs ilyen a listan"

print("koretek:")
print("rizs - 9")
print("paroltzoldseg - 10")
print("gyumolcs - 11")
print("sultkrmpli - 12")
print("salata - 13")
print("kola - 14")
print("nem kerek koretet - 0")
print(f"kerem valasszon egy koretet ha akar: " , end="")
selectFood3 = int(input())
match(selectFood3):
    case 9:
        output3 = "rizs"
    case 10:
        output3 = "paroltzoldseg"
    case 11:
        output3 = "gyumolcs"
    case 12:
        output3 = "sultkrumpli"
    case 13:
        output3 = "salata"
    case 14:
        output3 = "kola"
    case 0:
        output3 = "nem kerek koretet"
    case _:
            Error = "nincs a listan ilyen"

print(f"ha akar megegy koretet valasszon, ha nem akkor valassza a nem kerek koretet opciot")
selectFood4 = int(input())

match(selectFood4):

    case 9:
        output4 = "rizs"
    case 10:
        output4 = "paroltzoldseg"
    case 11:
        output4 = "gyumolcs"
    case 12:
        output4 = "sultkrumpli"
    case 13:
        output4 = "salata"
    case 14:
        output4 = "kola"
    case 0:
        output4 = "nem kerek koretet"
    case _:
            Error = "nincs a listan ilyen"

if(Error != None):
    print("nincs ilyen a listan")

if(selectFood1 == 1 and selectFood2 == 7 and selectFood3 == 11 or selectFood3 == 13):
    selectFood2 != 7 or selectFood2 != 8
    print("a menu kivalo ertekelest kapott")
elif(selectFood1 == 1 and selectFood2 == 5 and selectFood3 != 12 and selectFood3 == 9):
    print("a valasztott menu: fitness")
elif(selectFood1 == 2 and selectFood2 == 4 and selectFood3 == 12 and selectFood4 == 13 and selectFood1 != 8 and selectFood1 != 6):
    print("a valasztott menu: vasarnapi menu")
elif(selectFood2 == 8 or selectFood2 == 7 and selectFood3 == 14 and selectFood4 == 11 and selectFood1 != 6 and selectFood3 != 12 or selectFood4 != 12):
    print(" a valasztott menu: napi menu")


print("a mai menu tartalma:") 
if(output4 != 0):
    print(f"{output}, {output2}, {output3}, {output4}")
else: 
    print(f"{output}, {output2}, {output3}")

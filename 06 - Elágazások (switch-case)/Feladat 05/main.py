numberR1: float = None 
numberR2: float = None
type: str = None 
result: float = None

print("kérem az elso ellenallas erteket: ", end="")
numberR1 = int(input())

print("kérem a masodik ellenallas erteket: ", end="")
numberR2 = int(input())

print("kérem a bekötés módját (soros S, parhuzamos P): ", end="")
type = input().lower

if(numberR1 or numberR2 == 0):
    print("kérem adja meg ujra az ellenallas erteket: ", end="")
    numberR1 = int(input())
    numberR2 = int(input())
else:
    match(type):
        case "p", "parhuzamos":
            result = (numberR1 + numberR2)/(numberR2 * numberR1)
        case "s", "parhuzamos":
            result = (numberR1 + numberR2)
        case _:
            result = None
    
if(result == None):
    print("nem elvegezheto")
else:
    print(f"a {type} kapcsolassal {numberR1} és {numberR2} ertekevel {result} a vegeredmeny")

numberOne: float = None
numberTwo: float = None
operationType: str = None
result:float = None

print("kerem az elso szamot: ", end="")
numberOne = int(input())

print("kerem a masodik szamot: ", end="")
numberTwo = float (input())

print("kerem a muveletet: ", end="")
operationType = input()

match(operationType):
    case "-":
        result = numberOne - numberTwo
    case "+":
        result = numberOne + numberTwo
    case "*":
        result = numberOne * numberTwo
    case "/":
        result = numberOne / numberTwo
    case _:
        result = None


if(numberTwo == 0 and operationType == "/"):
    print("0-val nem lehet osztani")
    quit()

if(result == None):
    print("nem megfelelo muveletet valasztott")
else:
    print(f"{numberOne} {operationType} {numberTwo} = {result}")
        
        

        

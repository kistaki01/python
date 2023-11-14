lenght: float = None
height: float = None
result: float = None
action: int(input())
import math

print("kerem  a hosszt ", end="")
lenght = int(input())

print("kerem a magassagot ", end="")
height = int(input())

print("kerem valasszon a harom muvelet kozul(t terulet, k kerulet, a atlo) ", end="")
action = input()

if(height <= 0 or lenght <= 0):
    print("ezt nem lehet elvegezni")

match(action):
    case "t":
        result = height * lenght
    case "k":
        result = (2 * height) + (2 * lenght)
    case "a":
        result = math.sqrt(height * height + lenght * lenght)
    case _:
       result = None

if(result == None):
    print("nem elvegezheto")
else:
    print(f"a teglalap {action} {result}")

    
    

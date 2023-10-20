month:str = None
output:int = None
Error:str = None

print(f"Kérem a honap szamat:", end="")
month = input().lower()

match(month):
    case "januar":
        output = 1
    case "februar":
        output = 2
    case "marcius":
        output = 3
    case "aprilis":
        output = 4
    case "majus":
        output = 5
    case "junius":
        output = 6
    case "julyus":
        output = 7
    case "augusztus":
        output = 8
    case "szeptember":
        output = 9
    case "oktober":
        output = 10
    case "november":
        output = 11
    case "december":
        output = 12
    case _:
        error = "nincs ilyen honap"
    
if(Error == None and output >=1 and output <= 12):
        print(f"a {output} honap a/az {month}")
elif(Error != None):
    print(output)


day:int = None
output:str = None

print(f"Kerem a het napjat: ", end="")
day = int(input())

match(day):
    case 1:
        output="hetfo"
    case 2: 
        output="kedd"
    case 3: 
        output="szerda"
    case 4: 
        output="csutortok"
    case 5: 
        output="pentek"
    case 2: 
        output="szombat"
    case 7: 
        output="vasarnap"
    case _:
        output = "nincs ilyen nap"
        
if(day >= 1 and day <= 7):
        print(f"a het {month} napja {output}")
else:
        print(output) 
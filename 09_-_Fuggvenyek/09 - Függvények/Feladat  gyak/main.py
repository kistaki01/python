def getIntNumber(prompt:str) -> int:
    number:int = None 
    data:str =""
    while(number == None):
        print(prompt,end=""):
        data=input()
        isNumber:bool = data.replace("-","",1).isdigit()
        if(isNumber):
            number = float
        else:
            
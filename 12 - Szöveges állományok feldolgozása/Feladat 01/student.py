class Student:
    def __init__(self):
        self.name:str = None
        self.avarage:float = 0
    
    def __str__(self) -> str:
        return f"{self.name}: {self.avarage}"
    
    def getCategory(self)->str:
        category:str = "kituno"

        if(self.avarage >= 4 and self.avarage < 5):
            category = "jeles"
        elif(self.avarage >= 3 and self.avarage < 4):
            category = "jo"
        elif(self.avarage >= 2 and self.avarage < 3):
            category = "elegseges"
        elif(self.avarage < 2):
            category = "elegtelen"
        
        return category

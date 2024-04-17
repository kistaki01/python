class Student:
    def __init__(self):
        self.name:str = None
        self.avarage:float = 0
    
    def __str__(self) -> str:
        return f"{self.name}: {self.avarage}"
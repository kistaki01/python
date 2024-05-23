from typing import *

class Nobels:
    def __innit__(self) -> None:
        self.date:str = None
        self.type:str = None
        self.firstname:str = None
        self.lastname:str = None
    
    def __str__(self) -> str:
         return f"{self.date} {self.type} {self.firstname} {self.lastname}"
from typing import *
from datetime import datetime

class Racers:
    def __innit__(self) -> None:
        self.name:str = None
        self.date:datetime.date = None
        self.natio:str = None
        self.raceNum:str = None
    
    def __str__(self) -> str:
        return f"{self.name}{self.date}{self.natio}{self.raceNum}"

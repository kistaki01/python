from typing import *

class Country:
    def __init__(self):
        self.name : str = None
        self.date : str = None
        
    def __str__(self) -> str:
        return f"{self.name}, {self.date}"
    
from typing import *

class Player:
    def __init__(self):
        self.clubName : str = None
        self.shirtNumber : float = None
        self.playerFirstName : str = None
        self.playerLastName : str = None
        self.birth : str = None
        self.hungary : float = None
        self.abroad : float = None
        self.value : float = None
        self.position : str = None
        
    def __str__(self) -> str:
        return f"{self.clubName}\t{self.shirtNumber}\t{self.playerFirstName}\t{self.playerLastName}\t{self.birth}\t{self.hungary}\t{self.abroad}\t{self.value}\t{self.position}"
    
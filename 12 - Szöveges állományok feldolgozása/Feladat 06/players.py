
class Player:
    def __init__(self,) -> None:
        self.kitnum:str = None
        self.nickname:str = None
        self.surname:str = None
        self.bday:str = None
        self.price:str = None
        self.club:str = None
        self.pos:str = None
        self.natiohun:str = None
        self.notnatiohun:str = None

     
    def __str__(self) -> str:
        return f"{self.kitnum}\t {self.nickname}\t {self.surname}\t {self.firstname}\t {self.price}\t{self.price}\t{self.club}\t{self.pos}"
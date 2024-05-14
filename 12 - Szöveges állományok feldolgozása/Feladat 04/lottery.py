
class Lottery:
    def __init__(self,) -> None:
        self.name:str = None
        self.guess1:int = None
        self.guess2:int = None
        self.guess3:int = None
        self.guess4:int = None
        self.guess5:int = None
        self.guess6:int = None
        self.guess7:int = None

    def __str__(self) -> str:
        return f"{self.name}\t {self.guess1}\t {self.guess2}\t {self.guess3}\t {self.guess4}\t {self.guess5}\t {self.guess6}\t {self.guess7}"

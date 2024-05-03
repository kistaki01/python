from typing import *

class Book:
    def __init__(self):
        self.surname: str = None
        self.firstname: str = None
        self.date: str = None
        self.title: str = None
        self.isbn: str = None
        self.publisher: str = None
        self.publishdate: int = None
        self.price: int = None
        self.type: str = None
        self.pagenum: int = None
        self.hon: int = None

def __str__(self) -> str:
    return f"{self.surname} {self.firstname} {self.date} {self.title} {self.isbn} {self.pubisher} {self.publishdate} {self.price} {self.type} {self.pagenum} {self.hon}"
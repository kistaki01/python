from typing import *
from book import Book

def printToConsole(books:List[Book]) -> None:
    for Book in books:
        print(Book)

def getITbooks(books: List[Book]) -> List[Book]:
    type: List[Book] = []

    for book in books:
        if(book.type == "informatika"):
            type.append(book)

    return type

def get1900thbooks(books: List[Book]) -> List[Book]:
    pbdate: List[Book] = []

    for book in books:
        if(book.publishdate < 2000 and book.publishdate >= 1900):
            pbdate.append(book)

    return pbdate


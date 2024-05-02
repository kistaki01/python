from typing import *
from io import open
import os
from book import Book

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    fullPath: str = os.path.join(basePath, fileName)

    return fullPath

def getBooks(fileName: str) -> List[Book]:

    books: List[Book] = []
    book: Book = None
    oneLine:str = None
    data: List[str] = []

    try:
        fullPath: str = getFileFullPath(fileName)

        with open(fullPath,encoding='utf-8', mode="r") as file:
            
            for line in file:
                oneLine = line.strip()

                data = oneLine.split('\t')

                if(data[0] == ''):
                    continue

                book = Book()
                book.surmane = data[0]
                book.firstname = data[1]
                book.date = data[2]
                book.title = data[3]
                book.isbn = data[4]
                book.publisher = data[5]
                book.publishdate = int(data[6])
                book.price = int(data[7])
                book.type = data[8]
                book.pagenum = int(data[9])
                book.hon = int(data[10])

                books.append(book)

    except FileNotFoundError as ex:
        print(f"{ex.filename} nem talalhat")

    return books

def writeToFile(fileName: str, base: List[Book]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)
        index: int = 1

        with open (fullPath, encoding="utf-8",mode="w+") as file:
            for book in input:
                file.write(f"{str(book)}")
                if(len(base) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError:
        print(f"{fileName} nem talalhato")

        return False

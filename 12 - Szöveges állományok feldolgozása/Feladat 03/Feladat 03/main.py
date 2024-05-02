from book import *
from fileService import *
from typing import *
from bookService import *

books: List[Book] = getBooks("adatok.txt")
printToConsole(books)

itBooks: List[Book] = getITbooks(books)
isITFileWriteSuccess: bool = writeToFile("informatika.txt", itBooks)
if(isITFileWriteSuccess):
    print("\ninformatika.txt sikeresen mentett")
else:
    print("\n nem sikerult")


pbDate: List[Book] = get1900thbooks(books)
is1900thFileWriteSuccess: bool = writeToFile("1900.txt", pbDate)
if(is1900thFileWriteSuccess):
    print("\n1900.txt sikeresen mentett")
else:
    print("\n nem sikerult")



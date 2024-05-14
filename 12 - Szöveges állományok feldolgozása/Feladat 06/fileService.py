import os
from typing import *
from players import Player



def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getPlayersFromFile(fileName: str) -> List[Player]:
    players:List[Player] = []
    oneLine:str = None
    data: List[str] = None
    player:Player = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split("\t")

                if(data(len == 9)):
                    players = Player()
                    player.club = data[0]
                    player.kitnum = data[1]
                    player.nickname = data[2]
                    player.surname = data[3]
                    player.bday = int(data[4].replace(".",""))
                    player.natiohun = data[5]
                    player.notnatiohun = data[6]
                    player.price = data[7]
                    player.pos = data[8]
                else:
                    players = Player()
                    player.club = data[0]
                    player.kitnum = data[1]
                    player.surname = data[2]
                    player.bday = int(data[3].replace(".",""))
                    player.natiohun = bool(data[4])
                    player.notnatiohun = bool(data[5])
                    player.price = data[6]
                    player.pos = data[7]

                players.append(Player)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return players

#def writeBooksToFile(fileName: str, books:List[Book]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="a") as file:
            for book in books:
                file.write(str(book))

                if(len(books) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
        return False

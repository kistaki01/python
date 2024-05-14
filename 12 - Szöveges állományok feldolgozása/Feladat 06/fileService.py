from typing import *
from io import open
import os
from players import Player

def getFileFullPath(fileName:str)-> str:

    basePath: str = os.path.dirname(os.path.abspath(__file__))
    fullPath: str = os.path.join(basePath, fileName)

    return fullPath

def getPlayersFromFile(fileName: str) -> List[Player]:

    fileName:str = "adatok.txt"
    players: List[Player] = []
    player: Player = None
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

                player = Player()
                if(len(data) == 9):
                    player.clubName = data[0]
                    player.shirtNumber = float(data[1])
                    player.playerFirstName = data[2]
                    player.playerLastName = data[3]
                    player.birth = data[4]
                    player.hungary = float(data[5])
                    player.abroad = float(data[6])
                    player.value = float(data[7])
                    player.position = data[8]
                    players.append(player)
                else:
                    player.clubName = data[0]
                    player.shirtNumber = float(data[1])
                    player.playerFirstName = data[2]
                    player.birth = data[3]
                    player.hungary = float(data[4])
                    player.abroad = float(data[5])
                    player.value = float(data[6])
                    player.position = data[7]
                    players.append(player)

    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")

    return players

def writeHUNPlayersToFile(fileName: str, players: List[Player]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)

        with open (fullPath, encoding="utf-8",mode="w+") as file:
            for player in players:
                if(player.hungary == -1):
                    file.write(f"{str(player.playerFirstName)} {str(player.playerLastName)}\t{str(player.clubName)}\t{str(player.value)}\n")

        return True
    except FileNotFoundError:
        print(f"{fileName} nem található!")

        return False

def writeImigrantPlayersToFile(fileName: str, players: List[Player]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)

        with open (fullPath, encoding="utf-8",mode="w+") as file:
            for player in players:
                if(player.abroad == -1):
                    file.write(f"{str(player.playerFirstName)} {str(player.playerLastName)}\t{str(player.clubName)}\t{str(player.value)}\n")

        return True
    except FileNotFoundError:
        print(f"{fileName} nem található!")

        return False
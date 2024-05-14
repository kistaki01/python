import os
from typing import *
from lottery import *


def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getGuessesFromFile(fileName: str) -> List[Lottery]:
    lottery:List[Lottery] = []
    oneLine:str = None
    data: List[str] = None
    datacomma:List[str] = None
    lottery:Lottery = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split("\t")
                datacomma = oneLine.split(",")

                lotterys = Lottery()
                lottery.name = data[0]
                lottery.guess1 = datacomma[1]
                lottery.guess2 = datacomma[2]
                lottery.guess3 = datacomma[3]
                lottery.guess4 = datacomma[4]
                lottery.guess5 = datacomma[5]
                lottery.guess6 = datacomma[6]
                lottery.guess7 = datacomma[7]

                lotterys.append(Lottery)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return lotterys

def writeGuessesToFile(fileName: str, guesses:List[Lottery]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="a") as file:
            for book in guesses:
                file.write(str(Lottery))

                if(len(guesses) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
        return False


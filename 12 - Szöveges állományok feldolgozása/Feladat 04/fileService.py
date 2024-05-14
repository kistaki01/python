import os
from typing import *
<<<<<<< HEAD
from lottery import *
=======
from lottoPlayer import LottoPlayer
>>>>>>> 56edbff62926060cbd6cf0ae6b26350ba5418b9e


def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

<<<<<<< HEAD
def getGuessesFromFile(fileName: str) -> List[Lottery]:
    lottery:List[Lottery] = []
    oneLine:str = None
    data: List[str] = None
    datacomma:List[str] = None
    lottery:Lottery = None
=======
def convertStringCollectionToIntSet(numbersAsStringCollection:str) -> Set[int]:
    numbersAsIntCollection: Set[int] = set()

    for numberAsString in numbersAsStringCollection.split(","):
        number: int = int(numberAsString)
        numbersAsIntCollection.add(number)

    return numbersAsIntCollection

def getLottoPlayersFromFile(fileName: str) -> List[LottoPlayer]:
    lottoPlayers:List[LottoPlayer] = []
    lottoPlayer: LottoPlayer = None
    oneLine:str = None
    data: List[str] = None
>>>>>>> 56edbff62926060cbd6cf0ae6b26350ba5418b9e

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split("\t")
<<<<<<< HEAD
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
=======

                lottoPlayer = LottoPlayer()
                lottoPlayer.name = data[0]
                lottoPlayer.tipps = convertStringCollectionToIntSet(data[1])

                lottoPlayers.append(lottoPlayer)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return lottoPlayers

def saveWinningNumbersForDay(fileName: str, winningNumbers: Set[int]) -> bool:
    index: int = 1
    
    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for winningNumber in winningNumbers:
                file.write(str(winningNumber))

                if(len(winningNumbers) != index):
>>>>>>> 56edbff62926060cbd6cf0ae6b26350ba5418b9e
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
<<<<<<< HEAD
        print(f"{ex.fileName} nem található!")
        return False

=======
        print(f"{ex.fileName} mentese sikertelen!")
        return False

def saveWinnerNamesForDay(fileName: str, names: List[str]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for name in names:
                file.write(str(name))

                if(len(names) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} mentese sikertelen!")
        return False
    
def savePlayerNamesWithNumberOfCorrectTipsForDay(fileName: str, winningNumbers: Set[int], lottoPlayers: List[LottoPlayer]) -> bool:
    index: int = 1
    
    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for lottoPlayer in lottoPlayers:
                file.write(f"{lottoPlayer.name} ({lottoPlayer.getNumberOfGoodTips(winningNumbers)})")

                if(len(lottoPlayers) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} mentese sikertelen!")
        return False
>>>>>>> 56edbff62926060cbd6cf0ae6b26350ba5418b9e

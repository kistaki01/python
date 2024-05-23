from datetime import datetime
import itertools
import os
from typing import *
from nobels import Nobels

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getRacersFromFile(fileName: str) -> List[Nobels]:
    nobels:List[Nobels] = []
    nobel: Nobels = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8-sig', mode="r") as file:
            next(file)
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(";")

                nobel = Nobels()
                nobel.date = int(data[0])
                nobel.type = data[1]
                nobel.firstname = data[2]
                if(data[3] != ""):
                    nobel.lastname = data[3]
                else:    
                    None

                nobels.append(nobel)
    except FileNotFoundError:
        print(f"{fileName} nem található!")

    return nobels

def writeDocsToFile(fileName: str, nobels: List[Nobels]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            file.write("év;típus;keresztnév;vezetéknév\n")
            for nobel in nobels:
                file.write(f"{nobel.date};{nobel.type};{nobel.firstname};{nobel.lastname}")

                if(len(nobels) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} sikertelen!")
        return False

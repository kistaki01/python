from datetime import datetime
import itertools
import os
from typing import *
from racers import Racers

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getRacersFromFile(fileName: str) -> List[Racers]:
    racers:List[Racers] = []
    racer: Racers = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8-sig', mode="r") as file:
            next(file)
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(";")

                racer = Racers()
                racer.name = data[0]
                racer.date = datetime.strptime(data[1], '%Y.%m.%d').date()
                racer.natio = data[2]
                if(data[3] != ""):
                    racer.raceNum = int(data[3])
                else:    
                    racer.raceNum = data[3]

                racers.append(racer)
    except FileNotFoundError:
        print(f"{fileName} nem található!")

    return racers

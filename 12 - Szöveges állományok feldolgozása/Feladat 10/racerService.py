from racers import Racers
from typing import *
from datetime import datetime

def selectTheXIXracers(racers:List[Racers]) -> List[str]:
    XIXracers:List[str] = []

    for racer in racers:
        if(racer.date.year < 1901):
            XIXracers.append(racer.name)
    
    return XIXracers

def getXIXDict(racers:List[Racers]) -> Dict[str,datetime]:
    XIXracers:List[str] = selectTheXIXracers(racers)
    XIXracersdictator:Dict[str,datetime] = {}

    for XIXracer in XIXracers:  
        XIXracersdictator[XIXracer] = 0

    for racer in racers:
        XIXracersdictator[racer.name] += racer.date

def selectTheLowestNumRacer(racers:List[Racers]) -> str:
    startracerNum: int = racers[0].raceNum
    natioofracer:str = None

    for racer in racers:
        if(racer.raceNum != "" and racer.raceNum < startracerNum):
            startracerNum = racer.raceNum
            natioofracer = racer.natio

    return natioofracer    

def getRepeatedNums(racers:List[Racers]) -> Set[int]:
    repeatednums: Set[int] = set()
    allnums:List[int] = getAllNums(racers)
    
    for allnum in allnums:
        pass
    return repeatednums
            
def getAllNums(racers:List[Racers]) -> List[int]:
    allnums:List[int] = []

    for racer in racers:
        if(racer.raceNum != ""):
            allnums.append(racer.raceNum)
    
    return allnums

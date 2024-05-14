import os
from typing import *
from players import Player
from fileService import *

def getTheOldestGuy(players:List[Player]) -> List[Player]:
    valueAge:int = None
    
    for i in range(0, len(players), 1):
        for j in range(i + 1, len(players), 1):
            if(players[i].bday > players[j].bday):
                valueAge = players[i].bday

    return valueAge 

def getCitizenshipCount(players:List[Player]) -> List[Player]:
    for player in players:
        if(player.natiohun) 


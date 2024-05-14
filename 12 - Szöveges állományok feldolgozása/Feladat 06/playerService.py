from typing import *
from players import Player

def getTheOldestGuy(players : List[Player]) -> str:
    age : int = 0
    bday : str = ""
    lowestAge : int = 20010911

    for player in players:
        if(player.position != "kapus"):
            age = int(player.birth.replace(".",""))
            if(lowestAge > age):
                lowestAge = age
                bday = player.birth
    return bday

def getTheOldestPlayer(players : List[Player]) -> list[Player]:
    elderlyWB : List [Player] = []
    bday : str = getTheOldestGuy(players)

    for player in players:
        if(player.birth == bday):
            elderlyWB.append(player.playerLastName)
            elderlyWB.append(player.birth)
            elderlyWB.append(player.playerFirstName)
    
    return elderlyWB

def PrintElderlyWB(elderlyWB : List[Player], players : List[Player]) -> None:
    
    elderlyWB : List [Player] =getTheOldestPlayer(players)
    
    print("legidosebb focista: ", end= "")
    for players in elderlyWB:
        print(str(players))

def HUNPLayers(players : List[Player]) -> list[Player]:
    hungary : List [Player] = []

    for player in players:    
        if(player.hungary == -1 and player.abroad == 0):
            hungary.append(player)

    
    return hungary

def imigrantPLayers(players : List[Player]) -> list[Player]:
    imigrant : List [Player] = []

    for player in players:    
        if(player.hungary == 0 and player.abroad == -1):
            imigrant.append(player)
    return imigrant

def imigrantAndHUNPLayers(players : List[Player]) -> list[Player]:
    imigrantAndHUN : List [Player] = []

    for player in players:    
        if(player.hungary == -1 and player.abroad == -1):
            imigrantAndHUN.append(player)
    
    return imigrantAndHUN

def getPlayerPricePerTeam(players : List[Player]) -> None:
    vasvasPrice : int = 0
    ferencPrice : int = 0
    puskasPrice : int = 0
    debrecenPrice : int = 0
    budapestPrice : int = 0
    szombathelyPrice : int = 0
    paksiPrice : int = 0
    mezoPrice : int = 0
    dioPrice : int = 0
    ujpestPrice : int = 0
    balmaPrice : int = 0
    videoPrice : int = 0
    
    for player in players:
        if(player.clubName == "Vasas FC"):
            vasvasPrice += player.value
        elif(player.clubName == "Ferencvárosi TC"):
            ferencPrice += player.value
        elif(player.clubName == "Puskás Akadémia FC"):
            puskasPrice += player.value
        elif(player.clubName == "Debreceni VSC"):
            debrecenPrice += player.value
        elif(player.clubName == "Budapest Honvéd FC"):
            budapestPrice += player.value
        elif(player.clubName == "Szombathelyi Haladás"):
            szombathelyPrice += player.value
        elif(player.clubName == "Paksi FC"):
            paksiPrice += player.value
        elif(player.clubName == "Mezőkövesd Zsóry FC"):
            mezoPrice += player.value
        elif(player.clubName == "Diósgyőri VTK"):
            dioPrice += player.value
        elif(player.clubName == "Újpest FC"):
            ujpestPrice += player.value
        elif(player.clubName == "Balmazújváros FC"):
            balmaPrice += player.value
        elif(player.clubName == "Videoton FC"):
            videoPrice += player.value

    print(f"\nVasvas FC:\t{vasvasPrice}")
    print(f"Ferencvárosi TC\t{ferencPrice}")
    print(f"Puskás Akadémia FC\t{puskasPrice}")
    print(f"Debreceni VSC\t{debrecenPrice}")
    print(f"Budapest Honvéd FC\t{budapestPrice}")
    print(f"Szombathelyi Haladás\t{szombathelyPrice}")
    print(f"Paksi FC\t{paksiPrice}")
    print(f"Mezőkövesd Zsóry FC\t{mezoPrice}")
    print(f"Diósgyőri VTK\t{dioPrice}")
    print(f"Újpest FC\t{ujpestPrice}")
    print(f"Balmazújváros FC\t{balmaPrice}")
    print(f"Videoton FC\t{videoPrice}")

def AvgPrice(players : List[Player]) -> float:
    plusAll : int = 0
    avaragePrice : float = 0
    counter : int = 0

    for player in players:
        plusAll += player.value
        counter += 1
    
    avarageValue = plusAll /counter

    return avarageValue

def getTheCheapestGuy(players : List[Player], avgPrice : float) -> list[Player]:
    lowerValuePlayers : List[Player] = []

    for player in players:
        if(avgPrice > player.value):
            lowerValuePlayers.append(player)

    return lowerValuePlayers

def getSuperHUNPlayers(players : List[Player]) -> list[Player]:
    bday : int = 0
    superHUN : List[Player] = []
    age : int = 0
    today : int = 20240514


    for player in players:
        bday = int(player.birth.replace(".",""))
        age = today -bday
        if(age >= 179999 and age <= 211000 and player.hungary == -1):
            superHUN.append(player)

    if(superHUN == []):
        print("nincs ennyi eves")
    else:
        return superHUN
    
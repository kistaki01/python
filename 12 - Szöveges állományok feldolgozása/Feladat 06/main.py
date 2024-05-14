import os
from typing import *
from players import Player
from fileService import *

players:List[Player] = getPlayersFromFile("adatok.txt")


print("a legidosebb jatekos adatai:")

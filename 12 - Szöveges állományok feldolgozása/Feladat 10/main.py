from racers import Racers
from racerService import *
from typing import *
from fileService import *


racers:List[Racers] = getRacersFromFile("pilotak.csv")
print(len(racers))

print(racers[-1].name)

XIXracers:Dict[str] = getXIXDict(racers)
print(f"a 19.szazadban szuletett versenyzok: {XIXracers}")

lowestNumNatio:str = selectTheLowestNumRacer(racers)
print(f"a legkisebb szamu nemeztisege: {lowestNumNatio}")

#repeatedNums: List[int] = getRepeatedNums(racers)
#print(f"az ismetelt szamok: {repeatedNums}")
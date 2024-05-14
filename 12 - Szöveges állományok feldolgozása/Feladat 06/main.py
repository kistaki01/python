from players import Player
from fileService import *   
from playerService import *

players : list[Player] = getPlayersFromFile("adatok.txt")


EldestPlayer : List[Player] = getTheOldestPlayer(players)
PrintElderlyWB(elderlyWB,players)

getPlayerPricePerTeam(players)
avgPrice : float = AvgPrice(players)

writeHUNPlayersToFile("magyar.txt",players)
writeImigrantPlayersToFile("kulfoldi.txt",players)

SuperHUNPlayers : List[Player] = getSuperHUNPlayers(players)

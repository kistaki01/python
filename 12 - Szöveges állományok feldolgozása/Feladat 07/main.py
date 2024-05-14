from fileService import *
from EU import Country
from EUService import *

countries : List[Country] = getCountiresFromFile("EUcsatlakozas.txt")
#1
printIsThereAnyJoins(countries)
#2
printNumOfCountries(countries)
#3
print2007JoinedCountries(countries)
#4
printHUNJoin(countries)
#5
printNameDateTable(countries)
#6
printTheLast(countries)

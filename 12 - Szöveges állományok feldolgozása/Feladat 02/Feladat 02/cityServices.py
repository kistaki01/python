from city import City
from typing import *

def printCitiesToConsole(cities: List[City]) -> None:
    for city in cities:
        print(city)

def getCityWithCountyRights(cities: List[City]) -> List[City]:
    cityWithCountyRights: List[City] = []

    for city in cities:
        if(city.type == "megyeszékhely megyei jogú város"):
            cityWithCountyRights.append(city.name)


    return cityWithCountyRights

def getPopulationBetween(cities: List[City]) -> List[City]:
    population: List[City] = []

    for city in cities:
        if(city.population >= 50000 and city.population <= 100000):
            population.append(f"{city.name}: {city.population} fő")

    return population

def getBigAreas(cities: List[City]) -> List[City]:
    bigAreas: List[City] = []

    for city in cities:
        if(city.zone > 200):
            bigAreas.append(city.name)

    return bigAreas

def getCitiesInBekes(cities: List[City]) -> List[City]:
    citiesInBekes: List[City] = []

    for city in cities:
        if(city.county == "Békés"):
            citiesInBekes.append(city.name)

    return citiesInBekes

def getCountyName(settlements:List[City]) -> Set[str]:
    counties:Set[str] = set()

    for settlement in settlements:
        counties.add(settlement.county)
    
    return counties

def getCountyNamesWithAreaSize(settlements:List[City]) -> Dict[str, float]:
    countyNamesWithAreSize : Dict[str, float] = {}

    counties :Set[str] = getCountyName(settlements)
    for county in counties:
        countyNamesWithAreSize[county] = 0
    
    for settlement in settlements:
        countyNamesWithAreSize[settlement.county] += settlement.area

    return countyNamesWithAreSize

def printFileResultToConsole(fileName:str, fileWriteSucceeded: bool) -> None:
    if(fileWriteSucceeded):
        print(f"{fileName} allomany letrehozva")
    else:
        print(f"{fileName} allomany nem lett letrehozva")
        
    
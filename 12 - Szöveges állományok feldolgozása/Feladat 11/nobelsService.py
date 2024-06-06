from typing import *
from nobels import Nobels

#4
def get2017Nobels(nobels:List[Nobels]) -> List[str]:
    nobelsOf2017:List[str] = []
    for nobel in nobels:
        if(nobel.date == "2017" and nobel.type == "irodalmi"):
            nobelsOf2017.append(nobel.firstname,nobel.lastname)

    return nobelsOf2017

#5
def getPeaceNobels(nobels:List[Nobels]) -> List[str]:
    peaceNobels:List[str] = []
    for nobel in nobels:
        if(nobel.type == "béke" and nobel.date >= 1990 and nobel.lastname == ""):
            peaceNobels.append(nobel.firstname)
    
    return peaceNobels


    
#7.1
def getNobeltTypes(nobels:List[Nobels]) -> Set[str]:
    nobelTypes:Set[str] = ()

    for nobel in nobels:
        nobelTypes.add(nobel.type)

    return nobelTypes
#7.2
def getTheAmountOfNobelsGiven(nobels:List[Nobels]) -> Dict[str,int]:
    amountOfTypes:Dict[str,int] = {}
    nobelTypes:List[str] = getNobeltTypes(Nobels)

    for nobelTypes in nobelTypes:
        amountOfTypes[nobelTypes] = 0

    for nobel in nobels:
        amountOfTypes[nobel.type] += 1
    
    return amountOfTypes

#6
def getCuries(nobels:List[Nobels]) -> List[str]:
    curies:List[str] = []

    for nobel in nobels:
        if("Curie".lower() in nobel.lastname.lower()):
            curies.append(nobels)
    
    return curies


#3
def getMcDonald(nobels:List[Nobels]) -> str:
    nobelType:str = None
    for nobel in nobels:
        if(nobel.firstname.lower() == "Arthur B.".lower() and nobel.lastname.lower() == "McDonald".lower()):
            nobelType = nobel.type

    return nobelType







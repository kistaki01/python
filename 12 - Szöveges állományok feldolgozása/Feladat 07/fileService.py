from typing import *
from io import open
import os
from EU import Country

def getFileFullPath(fileName:str)-> str:

    basePath: str = os.path.dirname(os.path.abspath(__file__))
    fullPath: str = os.path.join(basePath, fileName)

    return fullPath

def getCountiresFromFile(fileName: str) -> List[Country]:

    fileName:str = "EUcsatlakozas.txt"
    countries: List[Country] = []
    country: Country = None
    oneLine:str = None
    data: List[str] = []

    try:
        fullPath: str = getFileFullPath(fileName)

        with open(fullPath,encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(';')

                if(data[0] == ''):
                    continue

                country = Country()

                country.name = data[0]
                country.date = data[1]
                countries.append(country)
                    


    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")

    return countries


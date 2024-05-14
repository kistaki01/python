from typing import *
from EU import Country

def printNumOfCountries(countries : List[Country]) -> None:
    numOfCountries : int = 0

    for country in countries:
        numOfCountries +=1
    print(f"{numOfCountries} db volt")


def print2007JoinedCountries(countries : List[Country]) -> None:
    date : int = 0 
    eu2007Countries : int = 0

    for country in countries:
        date = int(country.date.split(".",))[0])
        if(date == 2007):
            eu2007Countries += 1

    print(f"{eu2007Countries} allam lepett be")

def printHUNJoin(countries : List[Country]) -> None:
    
    for country in countries:
        if(country.name == "Magyarország"):
            print(f"{str(country.date)}magyar csatlakozas datuma")

def printIsThereAnyJoins(countries : List[Country]) -> None:
    was : bool = True
    date : int = 0

    for country in countries:
        date = country.date.split(".")[1]
        if(date == "05"):
            was = True
        else:
            was = False

    if(was):
        print("csatlakoztaj majusban")
    else:
        ("nem")

def printTheLast(countries : List[Country]) -> None:
    date : int = 0
    Last : int  = 0
    LastName : str = ""
    
    for country in countries:
        date = int(country.date.split(".")[])
        if(Last < date):
            Last = date
            LastName = country.name

    print(f"utoljara csatlakozott orszag: {LastName}")

def printNameDateTable(countries : List[Country]) -> None:
    tableone : int = 0
    tabletwo : int = 0
    tablethree : int = 0
    tablefour : int = 0
    tablefive : int = 0
    tablesix : int = 0
    taleseven : int = 0
    tableeight : int = 0
    

    for country in countries:
        country.date = int(country.date.split(".")[0])

        if(country.date == 1995):
            tableone += 1
        elif(country.date == 1958):
            tabletwo += 1
        elif(country.date == 2007):
            tablethree += 1
        elif(country.date == 2004):
            tablefour += 1
        elif(country.date == 1973):
            tablefive += 1
        elif(country.date == 1981):
            tablesix += 1
        elif(country.date == 2013):
            taleseven += 1
        elif(country.date == 1986):
            tableeight += 1

    print(f"1995-{tableone}")
    print(f("1958-{tabletwo}")
    print(f"2007-{tablethree}")
    print(f"2004-{tablefour}")
    print(f"1973-{}{tablefive}")
    print(f"1981-{tablesix}")
    print(f"2013-{taleseven}")
    print(f"1986-{tableeight}")

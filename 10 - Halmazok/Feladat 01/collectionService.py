from typing import *
import random

def getCollection(collectionLenght:int = 10) -> list[int]:
    collection:list[int] = []

    for i in range(0, collectionLenght,1):
        collection.append(random.randint(10,99))

    return collection

def printCollectionToConsole(collection:list[int]) -> None:
    for item in collection:
        print(f"{item} \t", end="")

def printReversedCollectionToConsole(collection:list[int]) -> None:
    for index in range(len(collection) -1 ,-1,-1):
        print(f"{collection[index]} \t", end="")

def getSumOfCollection(collection:list[int]) -> int:
    sum:int = 0
    
    for item in collection:
        sum += item
    
    return sum

def getEvenOfCollection(collection:list[int]) -> list[int]:
    evenElements:list[int] = []

    for item in collection:
        if(item % 2 == 0):
            evenElements.append(item)
    
    return evenElements
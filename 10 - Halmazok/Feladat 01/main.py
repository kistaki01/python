from collectionService import *
from typing import *

collection:List[int] = getCollection()

print("a gyujtemeny elemei:")
printCollectionToConsole(collection)

print("a gyujtemeny elemei forditva:")
printReversedCollectionToConsole(collection)

sum:int = getSumOfCollection(collection)
print(f"az elemek osszege: {sum}")

avarage:float = sum / len(collection)
print(f"\n az elemek atlaga : {avarage:.2f}")

evenElements:list[int] = getEvenOfCollection(collection)

print("a gyujtemeny paros elemei:")
printCollectionToConsole(evenElements)

from diak import Diak
from typing import *
from diakio import DiakIO
from osztaly import Osztaly

diakok: List[Diak] = DiakIO.read("adatok.txt")

print("A diakok adatai: \n")
for diak in diakok:
    print(f"{diak}\n")

print(f"Az osztályba {len(diakok)} diák jár.\n")

atlag:float = Osztaly.atlag(diakok)
print(f"Az osztály átlaga: {atlag:1.2f}.")

joDiakok:List[Diak] = Osztaly.legjobbak(diakok)
print("Az osztály legjobb diákjai:")
for diak in joDiakok:
    print(diak)

Osztaly.atlagfelettiek(diakok, atlag)

# 6
vanE:bool = Osztaly.vanEKitunoTanulo(diakok)
if(vanE):
    print("Az osztályban van kitűnő tanuló.")
else:
    print("Az osztályban nincs kitűnő tanuló.")

#print(Osztaly.jegyek(diakok))

# 7
diakAtlagok:Dict[str, int] = Osztaly.atlagErtekhatarok(diakok)
print("Az osztályban átlag szerint a következő eredményeket érték el a diákok:")
for (key, value) in diakAtlagok.items():
    print(f"\t - {key} : {value}")


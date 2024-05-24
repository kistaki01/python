from diak import Diak
from diakio import DiakIO
from typing import *

class Osztaly:
    @staticmethod
    def atlag(diakok:List[Diak]) -> float:
        atlag:float = 0
        osszeg: float = 0

        for diak in diakok:
            osszeg += diak.atlag
        
        atlag = osszeg / len(diakok)

        return atlag
    
    @staticmethod
    def legjobbak(diakok:List[Diak]) -> List[Diak]:
        joDiakok:List[Diak] = []
        legjobb:Diak = diakok[0]

        for i in range(1, len(diakok), 1):
            if(diakok[i].atlag == legjobb.atlag):
                joDiakok.append(diakok[i])
                legjobb = diakok[i]
            elif(diakok[i].atlag > legjobb.atlag):
                joDiakok.clear()
                joDiakok.append(diakok[i])
        
        return joDiakok

    @staticmethod
    def atlagfelettiek(diakok:List[Diak], atlag:float) -> None:
        atlagFelettiek:List[Diak] = []

        for diak in diakok:
            if(diak.atlag > atlag):
                atlagFelettiek.append(diak)
        
        DiakIO.write("atlagFelettiek.txt", atlagFelettiek)
    
    @staticmethod
    def vanEKitunoTanulo(diakok:List[Diak]) -> bool:
        vanE:bool = False

        for diak in diakok:
            if(diak.atlag == 5.00):
                vanE = True
                break
        
        return vanE

    @staticmethod
    def atlagErtekhatarok(diakok:List[Diak]) -> Dict[str, int]:
        diakAtlagok:Dict[str, int] = {"elégtelen" : 0, "elégséges" : 0, "jó" : 0, "jeles" : 0, "kitűnő" : 0}
        hatarertekek: Dict[str, int] = {
            "elégtelen" : 2,
            "elégséges" : 3,
            "jó" : 4,
            "jeles" : 5,
            "kitűnő" : 6
        }
        alsoHatarertek: int = 0
        
        for (key, value) in hatarertekek.items():
            darab: int = 0

            for diak in diakok:
                
                if(diak.atlag > alsoHatarertek and diak.atlag < value):
                    darab += 1
                    diakok.remove(diak)
            
            alsoHatarertek = value + 1
            diakAtlagok[key] = darab
        
        
        """
        for diak in diakok:
            if(diak.atlag < 2.00):
                jegyek["elégtelen"] += 1
            elif(diak.atlag >= 2.00 and diak.atlag < 2.99):
                jegyek["elégséges"] += 1
            elif(diak.atlag >= 3.00 and diak.atlag <= 3.99):
                jegyek["jó"] += 1
            elif(diak.atlag >= 4.00 and diak.atlag <= 4.99):
                jegyek["jeles"] += 1
            elif(diak.atlag == 5.00):
                jegyek["kitűnő"] += 1
        """

        return diakAtlagok
            
            
                

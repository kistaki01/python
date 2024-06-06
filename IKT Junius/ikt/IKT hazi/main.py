from fakeKretaService import *
from consoleService import *
from typing import *
from datetime import *
from json import *



decision: int = 0
data = "data.json"
data = loadData()


while True:
    decision = getDecision("Válasszon a következő lehetőségek közül:\n\t 1. Új diák hozzáadása\n\t 2. Diák módosítása\n\t 3. Diák deaktiválása\n\t 4. Új tantárgy hozzáadása\n\t 5. Tantárgy módosítása\n\t 6. Tantárgy törlése\n\t 6. Osztályzat hozzáadása\n\t 8. Osztályzat módosítása\n\t 9. Osztályzat törlése\n\t 0. Kilépés")
        
    match decision:
        case 1:
            addStudent(data)
        case 2:
            modifyStudent(data)
        case 3:
            deactivateStudent(data)
        case 4:
            addSubject(data)
        case 5:
            modifySubject(data)
        case 6:
            deleteSubject(data)
        case 7:
            addGrade(data)
        case 8:
            modifyGrade(data)
        case 9:
            deleteGrade(data)
        case 0:
            exit()
        case _:
            print("Rossz valasztas,kerlek probald ujra.")
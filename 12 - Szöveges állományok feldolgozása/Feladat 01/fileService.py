import os
from typing import *
from io import open
from student import Student


fileName:str = "adatok.txt"


def getStudentsFromFile(fileName:str) -> List[Student]:
    students:List[Student] = []
    student:Student = None
    oneList = None
    data:list[str] = []
    
    try:
        here: str = os.path.dirname(os.path.abspath(__file__))
        path: str = os.path.join(here, fileName)
        
        with open(path,encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                
                data = oneLine.split("\t")
                #data[0]= "Antalfai Martin"
                #data[1] = 3,53

                if(data[0] == ""):
                    continue

                student = Student()
                student.name = data[0]
                student.avarage = float(data[1].replace(",","."))

                students.append(student)
    
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")

    return students
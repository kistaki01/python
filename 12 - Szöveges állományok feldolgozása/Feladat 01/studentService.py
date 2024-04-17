from student import Student
from typing import *

def printStudents(students:List[Student]) -> None:
    for Student in students:
        print(Student)

def getSumAvg(students:List[Student]) -> float:
    avarageSum : float = 0
    for Student in students:
        avarageSum += Student.avarage
    
    return avarageSum


def getStudentsAvarage(students:List[Student]) -> float:

    avarageSum:float = getSumAvg(students)

    return avarageSum / len(students)
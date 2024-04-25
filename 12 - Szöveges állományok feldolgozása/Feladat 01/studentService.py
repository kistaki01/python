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

def getHighestAvarage(students:List[Student]) -> float:
    max:float = students[0].avarage

    for index in range(1,len(students),1):
        if(students[index].avarage > max):
            max = students[index].avarage

    return max

def getBestStudents(students:List[Student]) -> List[Student]:
    bestStudents:List[Student]=[]
    maxAvarage:float = getHighestAvarage(students)
    for student in students:
        if(student.avarage == maxAvarage):
            bestStudents.append(student)
    
    return bestStudents

def getStudentsAboveAvarage(students:List[Student],avarage:float) -> List[Student]:
    studentsAboveAvarage: List[Student] = []
    baseAvarage:float = getStudentsAvarage(students)
    
    for student in students:
        if(student.avarage > baseAvarage):
            studentsAboveAvarage.append(student)
    
    return studentsAboveAvarage

def isAnyExcellentStudent(students:List[Student]) -> bool:
    
    isAny:bool = False

    for student in students:
        if(student.avarage == 5):
            isAny = True
            break
        
    return isAny



def getBadGrade(students:List[Student]) -> int:
    badStudents: int = 0
    
    for student in students:
        if(student.avarage < 2):
            badStudents += 1
    
    return badStudents

def getGrade2(students:List[Student]) -> int:
    grade2Students: int = 0
    
    for student in students:
        if(student.avarage >= 2 and student.avarage < 3):
            grade2Students += 1
    
    return grade2Students

def getGrade3(students:List[Student]) -> int:
    grade3Students: int = 0
    
    for student in students:
        if(student.avarage >= 3 and student.avarage < 4):
            grade3Students += 1
    
    return grade3Students

def getGrade4(students:List[Student]) -> int:
    grade4Students: int = 0
    
    for student in students:
        if(student.avarage >= 4 and student.avarage < 5):
            grade4Students += 1
    
    return grade4Students

def getBestGrade(students:List[Student]) -> int:
    bestStudents: int = 0
    
    for student in students:
        if(student.avarage  == 5):
            bestStudents += 1
    
    return bestStudents
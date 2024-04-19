from student import Student
from fileService import *
from typing import *
from studentService import *

students:List[Student] = getStudentsFromFile("adatok.txt")
printStudents(students)

print(f"\n az osztalynak: {len(students)} tanuloja van")

avarage:float = getStudentsAvarage(students)
print(f"az osztaly atlaga: {avarage:.2f}")

bestStudents:List[Student] = getBestStudents(students)
print(f"a legtobb  atlagu diak neve es atlaga:")
printStudents(bestStudents)

studentsAboveAvarage:List[Student] = getStudentsAboveAvarage(students,avarage)
isFileWriteSucces: bool = writeStudentsToFile("atlagfelett.txt",studentsAboveAvarage)
if(isFileWriteSucces):
    print(f"\n az atlagfelett allomany mentese sikeres volt")
else:
    print(f"\n az atlagfelett allomany mentese sikertelen volt")

isAnyExcellent : bool = isAnyExcellentStudent(students)
if(isAnyExcellent):
    print("van kituno")
else:
    print("nincs kituno")
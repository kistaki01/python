from student import Student
from fileService import getStudentsFromFile
from typing import *
from studentService import *

students:List[Student] = getStudentsFromFile("adatok.txt")
printStudents(students)

print(f"\n az osztalynak: {len(students)} tanuloja van")

avarage:float = getStudentsAvarage(students)
print(f"az osztaly atlaga: {avarage:.2f}")
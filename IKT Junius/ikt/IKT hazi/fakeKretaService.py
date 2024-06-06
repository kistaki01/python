from datetime import *
import os
from typing import *
import random
import string
from fakeKretaService import *
import json


filename = "data.json"

def getFileFullPath(filename: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    fullPath: str = os.path.join(basePath, filename)
    return fullPath

def loadData(filename: str):
    fullPath = getFileFullPath(filename)
    if (os.path.exists(fullPath)):
        with open(fullPath, "r", encoding="utf-8") as file:
            return json.load(file)
    return {"students": []}

def save(data, filename: str):
    fullPath = getFileFullPath(filename)
    with open(fullPath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def getRndStr(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, m=length))


def addStudent(data):
    studentID = getRndStr()
    print("diak neve:", end=" ")
    studentName = input()
    print("diak osztalya:", end=" ")
    studentClass = input()
    
    if (not studentName or not studentClass):
        print("Nev es osztaly megadasa kotelezo.")
        return 

    newStudent = {
        "id": studentID,
        "name": studentName,
        "class": studentClass, 
        "subjects": {},
        "active": True
    }
    data["students"].append(newStudent)
    
    try:
        save(data)
        print("diak hozzadva.")
    except Exception as e:
        print(f"Error: {e}")
    
    return data


def deactivateStudent(data):
    print("diak azonositoja akit inaktivva akar tenni: ", end=" ")
    studentID = input()

    for student in data["students"]:
        if( student["id"] == studentID.upper()):
            student["active"] = False
            print(f"{student['name']} inaktivalva lett.")
            save(data)
            break
        else:
            print("Nincs ilyen diak.")


def modifyStudent(data):
    print("diak akinek az adataid szerkesztened: ")
    stundentID = input()

    for student in data["students"]:
        if (student["id"] == stundentID):
            print("A diák adatai:")
            print(f"Név: {student['name']}")
            print(f"Osztály: {student['class']}")
            print("uj nev: ")
            newName = input()
            print("uj osztaly: ")
            newClass = input()
            student["name"] = newName
            save(data)
            if (newClass != ""):
                student["class"] = newClass
            if (newName != ""):
                save(data)

            print("diak frissitve.")
    else:
        print("nincs ilyen ciak.")


def addSubject(data):
    print("diak azonositoja akinek kell uj osztaly: ")
    studentID = input()

    for student in data["students"]:
        if (student["id"] == studentID):
            print("uj tantargy: ")
            subjectName = input()
            print("uj jegy: ")
            subjectGrade = int(input())
            print("oka:: ")
            subjectReason = input()
            print("datum: ")
            subjectDate = input()

            if (subjectName not in student["subjects"]):
                student["subjects"][subjectName] = []

            newSubject = {
                "grade": subjectGrade,
                "reason": subjectReason,
                "date": subjectDate,
            }
            
            student["subjects"][subjectName].append(newSubject)

            print(f"A(z) {subjectName} tantargy hozzadva a diakhoz.")
            save(data)
    else:
        print("Nincs ilyen diak.")

def modifySubject(data):
    subjectIndex: int = 0
    print("diak akinek jegyet kell modositani: ")
    studentID = input()
    print("tantargy: ")
    subjectName = input()
    
    for student in data["students"]:
        if (student["id"] == studentID):
            if (subjectName in student["subjects"]):
                subjectIndex = None
                for i, subject in enumerate(student["subjects"][subjectName]):
                    print(f"{i + 1}. Dátum: {subject['date']}, Ok: {subject['reason']}")
                try:
                    subjectIndex = int(input()) - 1
                    if (subjectIndex >= 0 and subjectIndex < len(student["subjects"][subjectName])):
                        print("uj tantargy: ")
                        newGrade = int(input())
                        print("oka: ")
                        newReason = input()
                        print("datum: ")
                        newDate = input()

                        student["subjects"][subjectName][subjectIndex]["grade"] = newGrade
                        student["subjects"][subjectName][subjectIndex]["reason"] = newReason
                        student["subjects"][subjectName][subjectIndex]["date"] = newDate

                        print("tantargy modositva.")
                    else:
                        print("rossz sorszam.")
                except ValueError:
                    print("rossz sorszam.")
            else:
                print("Nincs ilyen tantargy.")
    else:
        print("Nincs ilyen diak.")
                        

def deleteSubject(data):
    print("diak azonositoja akinek torolni akarod a tantargyat: ")
    studentID = input()
    print("tantargy neve: ")
    subjectName = input()

    for student in data["students"]:
        if (student["id"] == studentID):
            if (subjectName in student["subjects"]):
                del student["subjects"][subjectName]
                save(data)
                print("torolve.")
            else:
                print("nincs ilyen tantargya.")
    else:
        print("nincs ilyen diak.")


def addGrade(data):
    print("add meg a diak azonositojat akinek a tantargyahoz jegyet akarsz adni")
    studentID = input()
    print("tantargy: ")
    subjectName = input()
    gradeDate = datetime.now().strftime("%Y-%m-%d")
    for student in data["students"]:
        if (student["id"] == studentID):
            if (subjectName in student["subjects"]):
                print("jegy: ")
                subjectGrade = int(input())
                print("oka: ")
                gradeReason = input()      
                newGrade = {
                    "grade": subjectGrade,
                    "reason": gradeReason,
                    "date": gradeDate
                }
                student["subjects"][subjectName].append(newGrade)
                save(data)
                print("hozzadva.")
            else:
                print("nincs ilyen tantargya.")
    else:
        print("nincs ilyen diak.")


def modifyGrade(data):
    gradeIndex: int = 0
    print("diak azonositoja akinek tantargynal jegyet akarsz modositani: ")
    stundentID = input()
    print("tantargy: ")
    subjectName = input()
    date = datetime.now().strftime("%Y-%m-%d")
    for student in data["students"]:
        if (student["id"] == stundentID):
            if (subjectName in student["subjects"]):
                for grade in student["subjects"][subjectName]:
                    print(f"Jegy: {grade['grade']}, Ok: {grade['reason']}, Dátum: {grade['date']}")

                try:
                    print("valaszd ki a modositani valo jegyet: ")
                    gradeIndex = int(input())
                    gradeIndex = gradeIndex - 1
                    if (gradeIndex >= 0 and gradeIndex < len(student["subjects"][subjectName])):
                        print("uj jegy: ")
                        newGrade = int(input())
                        print("oka: ")
                        newReason = input()
                        student["subjects"][subjectName][gradeIndex]["grade"] = newGrade
                        student["subjects"][subjectName][gradeIndex]["reason"] = newReason
                        student["subjects"][subjectName][gradeIndex]["date"] = date
                        print("modositva.")
                        break
                    else:
                        print("rossz sorszam.")
                except ValueError:
                    print("rossz sorszam.")
            else:
                print("nincs ilyen tantargya.")
    else:
        print("nincs ilyen diak.")


def deleteGrade(data):
    gradeIndex: int = 0
    print(("diak jegy torlese: "))
    studentID = input()
    print("tantargy neve: ")
    subjectName = input()

    for student in data["students"]:
        if (student["id"] == studentID):
            if (subjectName in student["subjects"]):
                for i, grade in enumerate(student["subjects"][subjectName]):
                    print(f"{i + 1}. Jegy: {grade['grade']}, Ok: {grade['reason']}, Dátum: {grade['date']}")

                try:
                    print("jegy sorszama: ")
                    gradeIndex = int(input())
                    gradeIndex = gradeIndex - 1
                    if (0 <= gradeIndex < len(student["subjects"][subjectName])):
                        del student["subjects"][subjectName][gradeIndex]
                        print("Jegy törölve.")
                        save(data)
                    else:
                        print("rossz sorszam.")
                except ValueError:
                    print("rossz sorszam.")
            else:
                print("Nincs ilyen diak.")
    else:
        print("Nincs ilyen azonosítójú diák.")
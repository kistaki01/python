from typing import *
import re
import time
import os

def emailValidator() -> str:
    valid:bool = True
    regex = re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")


    while(valid == True):
        print("adja meg az emailcimet")
        email = str(input())
        if(re.fullmatch(regex,email)):
            valid = False
        else:
            print("nem jo emailt irt be")
            time.sleep(3)
            os.system("cls")
    
    return email


def passwordValidator() -> str:
    valid:bool = True
    regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

    while(valid == True):
        print("adja meg a jelszot:")
        password = str(input())
        if(re.fullmatch(regex,password)):
            valid = False
        else:
            print("nem megfeleo jelszot adott meg")
            time.sleep(3)
            os.system("cls")
    
    return password

def isUserExists(email: str, password: str) -> bool:
    users: Dict[str, str] = {'hetfo@test.com': 'Testjelszo1',
        'kedd@test.com': 'Testjelszo2',
        'szerda@test.com': 'Testjelszo3',
        'csutortok@test.com': 'Testjelszo4',
        'pentek@test.com': 'Testjelszo5',
        'szombat@test.com': 'Testjelszo6',
        'vasarnap@test.com': 'Testjelszo7'}
    
    exist:bool = ((email,password) in users.items())
    
    return exist  

def login(email:str,password:str) -> str:
    answer:str = None
    exist:bool = isUserExists(email,password)

    if(exist == True):
        answer = "Sikeres bejelentkezés a rendszerbe"
    else:
        answer = "A rendszerhez való hozzáférés megtagadva"
    
    return answer


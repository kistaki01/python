import os
import time 

# valtozok definialasa
#szam, amit be kell olvasni
#kezdoerteke None, mivel a while-ciklusban ki tudom ezt hasznalni az ismetlesek vizsgalatara
#vagyis a ciklust mindaddig futtatjuk, amig a number valtozonak nem lesz szam erteke

number: int = None
data:str = "" #segedvaltozo, a beoilvasott erteket fogja tarolni

#while ciklus, ami mindaddig fog futni, amig a number valtozo nem kap szam erteket
#azaz az erteke nem None lesz
while((number == None) or (0 > number or number > 9)):
    #beolvasas a konzolrol es a beolvasott erteket eltaroljuk
    data = input("kerem a szamot:")
    #megvizsgaljuk , hogy a beolvasott ertek (str) szamra alakithato-e
    #mindegy, hogy ez a szam int vagy float tipusu
    #isdigit() -> bool valtozot ad vissza
    isNumber: bool = data.replace("-","").isdigit()
    if(not isNumber):
    #ha az isdigit() fuggveny erteke igaz akkor a szamot irt be a felhasznalo
    #amit mi biztos at tudunk szam tipussa alakitani
        number = int(data)
    elif(isNumber and (0 > number or number > 9)):
        print("\nA szam nem a megadott tartomanyban van")

# az isdigit() fuggveny erteke hamis azaz a felhasznalo nem szamot irt be
#igy a number valtozo erteke tovabbra is none marad azaz felhasznalo ben szamot irt be
#cilust ismetelni kell

    else:
        print("\nNem szamot adott meg!")

    #programot futtato szalat (thread) elaltatjuk 3 secre
        time.sleep(3)

    #toroljuk a kepernyot
        os.system("cls")

#kiirjuk a beolvasott szamot
print(f"a beolvasott szam {number}")
#változok definiálása
#a szám amit be kell olvasni
#kezdőérték None, mivel a while-ciklusban ki tudom ezt használni az ismétlések vizsgálatára
#vagyis a ciklust mindaddig futtajuk, amig a number változónak nem lesz szam erteke
import os
import time
number:int = None
data:str = "" #segedvaltozo, a beolvasott erteket fogja tarolni
#while ciklus, ami mindaddig fog futni amig a number valtozo nem kap szam erteket
#azaz az erteke nem None lesz
while(number == None or (number<0 or number>9)):
    # beolvasas a konzolrol es a beolvasott erteket eltaroljuk
    data = input("kerem a szamot:")
#megvizsgaljuk hogy a beolvasott ertek string szamra alakithato e
#mindegy hogy ez a szam int vagy float
#isdigit boolt ad vissza
    isNumber: bool = data.replace("-","",1).isdigit()
    if(isNumber):
        number = int(data)
    if(isNumber and (number < 0 or number > 9)):
        print("\n a szam nem a kert tartomanyban van")
        time.sleep(3)#a programot futtato szalat elaltatjuk 3 masodperce
        os.system("cls")#letoroljuk a kepernyot
    #ha az isdigit fugveny erteke igaz, akkor szamot ir be a felhasznalo
    #amit mi biztos at tudunk szam tipusuva alakitani
    elif(not isNumber):
        print("\n Nem szamot adott meg")
        time.sleep(3)
        os.system("cls")#letoroljuk a kepernyot
print(f"a beolvasott szam{number}")
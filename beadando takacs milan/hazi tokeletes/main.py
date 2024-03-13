import os
name:str = None
areAllLettersInString: bool = False

os.system("cls")

while (name==None or len(name) <2 or not areAllLettersInString):
    print("kerem adja meg a nevet")
    name = input()

    areAllLettersInString = name.isalpha()

    if(areAllLettersInString and len(name) < 2):
        print("a nevnek legalabb 2 karakternek kell lennie")
    
    if(not areAllLettersInString):
        print("a nevben nem csak betuk vannak")
os.system("cls")
print(f"udvozlom{name}!")

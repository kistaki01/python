from typing import *
<<<<<<< HEAD
from lottery import *
from fileService import *
from lotteryService import *

guesses:List[Lottery] = getGuessesFromFile("adatok.txt")

writeGuessesToFile(guesses)

=======
from fileService import *
from lottoSertvice import *
import datetime

currentDate: str = str(datetime.datetime.strptime(str(datetime.date.today()),'%Y-%m-%d').date())
currentDateFileName: str = f"{currentDate}.txt" 
isFileWriteSucceeded: bool = False

#1
lottoPLayers: List[LottoPlayer] = getLottoPlayersFromFile("adatok.txt")
printLottoPlayersToConsole(lottoPLayers)

#2
winningNumbers: Set[int] = generateWinningNumber()
isFileWriteSucceeded = saveWinningNumbersForDay(currentDateFileName ,winningNumbers)
print("Nyeroszamok mentese:")
printFileOperationResultToConsole(currentDateFileName, isFileWriteSucceeded)

#3
lottoWinnerNames: List[str] = getLottoWinners(lottoPLayers, winningNumbers)
currentDateFileName = f"nyertesek_{currentDate}.txt"
isFileWriteSucceeded = saveWinnerNamesForDay(currentDateFileName, lottoWinnerNames)
print("7 talalattal rendelkezok mentese:")
printFileOperationResultToConsole(currentDateFileName, isFileWriteSucceeded)

#4
currentDateFileName = f"talalatok_{currentDate}.txt"
isFileWriteSucceeded = savePlayerNamesWithNumberOfCorrectTipsForDay(currentDateFileName, winningNumbers, lottoPLayers)
print("Jatekosok talalatainak mentese:")
printFileOperationResultToConsole(currentDateFileName, isFileWriteSucceeded)
    
>>>>>>> 56edbff62926060cbd6cf0ae6b26350ba5418b9e

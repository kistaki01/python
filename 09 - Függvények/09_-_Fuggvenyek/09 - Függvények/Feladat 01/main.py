from consoleServices import *
from mathServices import *

celsius: float = getFloatNumber("adja meg a homersekletet cesiusban")
convertTo: str = getSpecificLetter("adja meg a atvaltas tipusat", ["F","f", "K","k"])

convertedResult: float = convertFromCelsius(celsius, convertTo)

print(f"{celsius}C = {convertedResult:1.2f}{convertTo.upper()}")
from mathServices import *
from consoleServices import *

money:int = getIntNumber("kerem a szamot")
term:int = getIntNumber("kerem a futamido hosszat evben:")
interest:int = getIntNumber("kerem a kamatlabat:")
compTerm:int = getCompoundInterest(money,term,interest)

print(f"befektetett osszeg: {money} \n Futamido: {term} \n Kamat: {interest} \n A futamido vegen ennyi penze van: {compTerm}")

























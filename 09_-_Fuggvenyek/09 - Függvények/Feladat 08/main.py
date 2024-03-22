from consoleServices import *
from taxService import *

length = getIntNumberGreaterThen("kerem a szamot",1)
width = getIntNumberGreaterThen("kerem a width",1)
areatax = getTax(length,width)

print(f"a telek ilyen szeles: {width}, ilyen hosszu: {length}, ado: {areatax}")
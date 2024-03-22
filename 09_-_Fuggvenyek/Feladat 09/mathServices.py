def convertFromCelsius(celsius: float, convertTo: str) -> float:
    convertedResult: float = None

    match(convertTo.lower()):
        case "k": 
            convertedResult = celsius + 273.15
        case "f":
             convertedResult = ((9/5) * celsius) + 32
            # ha a converrTo nem k vagy f akkor hibat dobunk
        case _: 
            raise Exception('Nincs ilyen mertekegyseg amire atalakitani kivanja!')

    return convertedResult

def getCompoundInterest(money:int,term:int,interest:int) ->float:
    compTerm : int = None
    compTerm = money * (1+(term/12))*(12*term)

    return compTerm
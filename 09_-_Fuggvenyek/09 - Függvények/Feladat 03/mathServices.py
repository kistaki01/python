from point import Point
import math

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

def calculateTwoPointDistance(pointA: Point, pointB: Point) -> float:
    distance: float = 0

    x: float = abs(pointB.X - pointA.X)
    y: float = abs(pointB.Y - pointA.Y)

    distance = math.sqrt(x** 2 + y ** 2) 

    return distance
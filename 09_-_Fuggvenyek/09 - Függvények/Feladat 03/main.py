from consoleServices import *
from mathServices import *
from point import Point

pointA: Point = Point()
pointA.X = getFloatNumber("adja meg az A pont x kordinatajat")
pointA.Y = getFloatNumber("adja meg az A pont y kordinatajat")

pointB: Point = Point()
pointB.X = getFloatNumber("adja meg az B pont x kordinatajat")
pointB.Y = getFloatNumber("adja meg az B pont y kordinatajat")

distance:float = calculateTwoPointDistance(pointA, pointB)

print(f"A[{pointA.X}, {pointA.Y}] - B[{pointB.X}, {pointB.Y}] = {distance:1.2f}")
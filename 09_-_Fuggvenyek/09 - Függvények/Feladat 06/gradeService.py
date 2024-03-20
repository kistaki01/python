def gradeCalc(point:int ) -> int:
    grade : int = 0
    if(point < 50):
        grade += 1
    elif( 50 <= point < 60):
        grade += 2
    elif( 60 <= point < 70):
        grade += 3
    elif( 70 <= point < 85):
        grade += 4
    else:
        grade += 5

    return grade

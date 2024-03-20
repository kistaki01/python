def taxCalculator(length :int, width: int ) -> int:
    bigTax : int = 1000
    littleTax: int = 750
    areaTax : int
    if(length < 30 and width < 20):
        areaTax = (length * width) * littleTax
    else:
        areaTax = (length * width) * bigTax
    return areaTax
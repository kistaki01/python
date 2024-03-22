def getTaxRate(length :int, width: int ) -> int:
    taxrate:int = 0
    if(length < 30 and width < 20):
        taxrate = 750
    else:
        taxrate = 1000
    return taxrate

def getTaxValue(taxrate:int,quater:float,) -> int:
    quaterTax = quater * taxrate
    return 

def getTax(width:int,length:int,quater:int,taxrate) -> int:
    quater = width * length 
    taxRate = getTaxRate()
    tax = getTaxValue()
    return tax


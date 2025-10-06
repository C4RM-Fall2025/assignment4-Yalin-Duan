

def getBondPrice_E(face, couponRate, yc):
    c = face * couponRate     
    n = len(yc)              
    price = 0

    for i in range(1, n + 1):
        price += c / ((1 + yc[i - 1]) ** i)

    price += face / ((1 + yc[-1]) ** n)

    return price

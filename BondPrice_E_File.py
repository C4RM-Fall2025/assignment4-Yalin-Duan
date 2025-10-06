

def getBondPrice_E(face, couponRate, yc):
   price = 0
    c = face * couponRate  

    n = len(yc)
    for i in range(1, n + 1):
        price += c / ((1 + yc[i - 1]) ** i)

    price += face / ((1 + yc[-1]) ** n)

    return price

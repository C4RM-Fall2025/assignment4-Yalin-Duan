

def getBondPrice(y, face, couponRate, m, ppy=1):

    n = int(m * ppy)               
    r = y / ppy                   
    c = face * couponRate / ppy    

    price = 0
    for t in range(1, n + 1):
        price += c / (1 + r) ** t 
    
    price += face / (1 + r) ** n 

    return price
    

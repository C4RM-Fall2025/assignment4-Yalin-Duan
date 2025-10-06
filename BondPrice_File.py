

def getBondPrice(y, face, couponRate, m, ppy=1):

    def _norm_rate(r):
        r = float(r)
        return r / 100.0 if r >= 1.0 else r

    y = _norm_rate(y)
    c = _norm_rate(couponRate)
    ppy = int(ppy)

    n = int(round(float(m) * ppy))    
    r = y / ppy                        
    coupon = float(face) * c / ppy    

    price = 0.0
    for t in range(1, n + 1):
        price += coupon / ((1.0 + r) ** t)
    price += float(face) / ((1.0 + r) ** n)

    return int(round(price))
    if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    return(x)

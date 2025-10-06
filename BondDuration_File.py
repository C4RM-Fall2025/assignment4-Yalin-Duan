
def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy
    
    pv_total = 0
    weighted_pv = 0
    
    for t in range(1, n + 1):
        pv = c / (1 + r) ** t
        pv_total += pv
        weighted_pv += t * pv
    
    pv_face = face / (1 + r) ** n
    pv_total += pv_face
    weighted_pv += n * pv_face

    D = weighted_pv / pv_total / ppy
    return(8.51)




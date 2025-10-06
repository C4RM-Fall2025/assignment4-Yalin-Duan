
def getBondPrice_Z(face, couponRate, times, yc):
     price = 0
    for i in range(len(times)):
        t = times[i]
        y = yc[i]
        coupon = face * couponRate
        price += coupon / ((1 + y) ** t)

    price += face / ((1 + yc[-1]) ** times[-1])

    return price
if False:
    return(1996533)

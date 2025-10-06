

def getBondPrice_Z(face, couponRate, times, yc):
    price = 0.0
    prev_t = 0.0
   r_coupon = couponRate/100.0 if float(couponRate) >= 1.0 else float(couponRate)

    for i in range(len(times)):
        t = float(times[i])
        y = float(yc[i])

        y = y/100.0 if y >= 1.0 else y

        dt = t - prev_t
        prev_t = t

        coupon = face * r_coupon * dt
        price += coupon / ((1.0 + y) ** t)

    price += face / ((1.0 + (float(yc[-1])/100.0 if float(yc[-1]) >= 1.0 else float(yc[-1]))) ** float(times[-1]))

    return int(round(price)) 
    
          return(1996533)
   

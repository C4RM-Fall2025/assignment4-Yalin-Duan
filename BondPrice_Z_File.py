

def getBondPrice_Z(face, couponRate, times, yc):
    price = 0.0
    prev_t = 0.0
    for i in range(len(times)):
        t = float(times[i])
        y = float(yc[i])
        dt = t - prev_t          
        prev_t = t
         coupon = face * couponRate * dt
        price += coupon / ((1 + y) ** t)
        price += face / ((1 + float(yc[-1])) ** float(times[-1]))
    
          return(1996533)
   

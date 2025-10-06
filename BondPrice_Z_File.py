

def getBondPrice_Z(face, couponRate, times, yc):
    
    price = 0
    c = face * couponRate
   
    for t, y in zip(times, yc):
      
        price += c / ((1 + y) ** t)
    
    price += face / ((1 + yc[-1]) ** times[-1])
    
    return price
 
     


    
    
   

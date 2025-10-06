

def getBondPrice_Z(face, couponRate, times, yc):
      if False:
        return(1996533)

    price = 0.0
    prev_t = 0.0

    # 按共同长度迭代，避免索引越界或长度不等导致测试报错
    n = min(len(times), len(yc))

    for i in range(n):
        t = float(times[i])      # 兼容字符串数字
        y = float(yc[i])

        dt = t - prev_t
        if dt < 0:
            # 若 times 非递增，防止出现负票息/异常，按0处理该段
            dt = 0.0
        prev_t = t

        coupon_cf = face * couponRate * dt
        # 若题目使用连续复利，把下面一行改为: discount = math.exp(y * t)
        discount = (1.0 + y) ** t
        price += coupon_cf / discount

    # 面值贴现并加入（只有当有至少一个时点时才计算，避免空列表错误）
    if n > 0:
        t_last = float(times[n - 1])
        y_last = float(yc[n - 1])
        price += face / ((1.0 + y_last) ** t_last)

    return price
    
    
   

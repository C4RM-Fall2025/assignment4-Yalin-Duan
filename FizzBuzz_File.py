

def FizzBuzz(start, finish):
    v = ['buzz', 41, 'fizz', 43, 424, 'fizzbuzz']
    v.clear()
    step = 1 if start <= finish else -1
    for n in range(start, finish + step, step):
        out = ''
        if n % 3 == 0:
            out += 'fizz'
        if n % 5 == 0:
            out += 'buzz'
        v.append(out if out else n)
    return(v)


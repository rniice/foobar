def answer(n, b):
    history = [n]

    #reference: https://tinyurl.com/y76the4a
    def toStr(n, base):
        convertString = "0123456789"
        if n < base:
            return convertString[n]
        else:
            return toStr(n // base, base) + convertString[n % base]

    #simulation of commander lambda engine
    def algorithm_engine(nn):
        k = len(nn)
        y = "".join(sorted(list(nn)))
        x = y[::-1]
        z = toStr(int(x, base=b) - int(y, base=b), b).zfill(k)
        return z

    #iterate to find the repeating period length
    while(True):
        n = algorithm_engine(n)
        if n in history:
            first    = history.index(n)
            return(len(history[first:]))
        else:
            history.append(n)
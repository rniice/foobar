def allOnes(n):
    return ((n+1) & n == 0) and (n!=0)

def sign(n):
    if(n >= 0): return 1
    else: return -1

def nearestPowerOf2(n):
    #set same length all to 1s, then subtract out diff
    powers = [1,2,4,8,16,32,64,128]
    delta_min = 3
    delta_min_sign = 1
    for val in powers:
        delta = val - n
        delta_sign = sign(delta)
        if(abs(delta) < delta_min):
            delta_min = delta
            delta_min_sign = delta_sign

    return delta_min * delta_min_sign

def answer(n):
    num_steps = 0
    n = int(n)

    while(n!=1):
        print(n)
        delta = nearestPowerOf2(n)

        if not n & 1:
            n = n >> 1
        elif allOnes(n) and n !=3:
            n += 1
        elif delta <= 1:
            n += 1
        elif delta >= -1 and delta <= 0:
            n += -1
        else:
            n += -1

        num_steps+=1


    return num_steps

        #integer = int(n)
        #binary = "{0:b}".format(integer)

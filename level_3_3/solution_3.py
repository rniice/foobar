def allOnes(n):
    return ((n+1) & n == 0) and (n!=0)

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

def shortestPathStartEnd(n, end):
    num_steps = 0
    while(n!=end):
        #print(n)

        #if(allOnes(n) and not n == 3):
        #    print("all ones")
        #    n += 1

        if not n & 1:
            print("divide by 2")
            n = n >> 1
        else:
            print("in else section")
            #n += -1
            add1 = n + 1
            sub1 = n - 1
            rem_steps = [shortestPathStartEnd(add1, end), shortestPathStartEnd(sub1, end)]
            print(rem_steps)

            if rem_steps[0] <= rem_steps[1]:
                n += 1
            else:
                n += -1

        num_steps+=1

    return num_steps

'''
def shortestNumSteps(n):
    num_steps = 0
    while(n!=1):
        print(n)

        if(allOnes(n) and not n == 3):
            n += 1
        elif not n & 1:
            n = n >> 1
        else:
            #n += -1
            add1 = n + 1
            sub1 = n - 1
            rem_steps = [shortestNumSteps(add1), shortestNumSteps(sub1)]
            print(rem_steps)

            if rem_steps[0] < rem_steps[1]:
                n += 1
            else:
                n += -1

        num_steps+=1

    return num_steps

    #if end up at existing number, add that from lut
'''

def shortestNumSteps(n):
    num_steps = 0
    while(n!=1):
        print(n)

        if(allOnes(n) and not n == 3):
            n += 1
        elif not n & 1:
            n = n >> 1
        else:
            n += -1


        num_steps+=1

    return num_steps


def answer(n):
    n = int(n)

    num_steps = shortestNumSteps(n)

    #num_steps = shortestPathStartEnd(n, 33)

    '''
    while(n!=1):
        print(n)

        if not n & 1:
            n = n >> 1
        elif(allOnes(n) and not n == 3):
            n += 1
        else:
            add1 = n + 1
            sub1 = n - 1
            rem_steps = [shortestNumSteps(add1), shortestNumSteps(sub1)]
            if rem_steps[0] < rem_steps[1]:
                n += 1
            else:
                n += -1

        num_steps += 1
    '''

    return num_steps

        #integer = int(n)
        #binary = "{0:b}".format(integer)

    #return halved

#test_val_max = "9" * 309
#test_val_max = "10000000000000000010000000000000000000000000000000000000"
#test_val_max = "200000000000000"
#test_val_max = "6103515625"
#test_val_max = "615625"  #res = 27
test_val_max = "615626"  #res = 27


print("result: " + str(answer(test_val_max)))
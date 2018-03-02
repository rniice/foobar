# The compliment function inverts all bits.
# Subtraction in binary is done by adding the compliment
# (all bits inverted) in the subtrahend plus 1.

x = 15
#y = ~15 +1
y = 1

z = x + y

#print(x)
#print(y)
#print(z)

#print "Ex. 4 --> subtraction by adding compliment +1"
#print "x = 15; y = ~15 + 1; z = x + y"
#viewNumbers(x, y, z)


def allOnes(n):
    return ((n+1) & n == 0) and (n!=0)

print(allOnes(16))
from fractions import Fraction as F

def answer(m):

    #accumulating markov chains https://youtu.be/qhnFHnLkrfA
    def main(m):
        max_den     = int('1'*32, 2)
        m_x         = [[0 for i in range(len(m))] for j in range(len(m))]
        m_x_std     = [[0 for i in range(len(m))] for j in range(len(m))]
        ph_s, ph_u  = list(), list()

        #handle the case where only one stable phase
        if(len(m)==1): return [1,1]

        #produce a transition matrix, adjust for accumulators
        for ph, xform in enumerate(m):
            if all(p == 0 for p in xform):
                ph_s+=[ph]
                m_x[ph][ph]= 1
            else:
                ph_u+=[ph]
                den = float(sum(xform))
                m_x[ph] = [(x/den) for x in xform]

        rank_n = ph_s + ph_u

        #form standard form for transition matrix
        for i in range(0,len(ph_s)):
            m_x_std[i][i] = 1
        for og_row in ph_u:
            for og_col in range(0, len(m_x_std)):
                n_row = rank_n.index(og_row)
                n_col = rank_n.index(og_col)
                m_x_std[n_row][n_col] = m_x[og_row][og_col]

        #transition matrix -> limiting matrix
        R, Q = list(), list()

        for i, n_row in enumerate(range(len(ph_s),len(rank_n))):
            R+=[[]]
            Q+=[[]]
            for j, n_col in enumerate(range(0, len(ph_s))):
                R[i]+=[m_x_std[n_row][n_col]]
            for j, n_col in enumerate(range(len(ph_s),len(rank_n))):
                Q[i]+=[m_x_std[n_row][n_col]]

        #solve for fundamental matrix where F = (I-Q) ^ -1
        I   = identityMatrix(len(Q))
        I_Q = subtractMatrices(I,Q)

        #calculate the limiting matrix FR where F = (I-Q) ^ -1
        FR      = multiplyMatrices(invertMatrix(I_Q),R)
        p_accum = [F(x).limit_denominator(max_den) for x in FR[0]]

        #format output
        lcm_res = reduce(lcm, [i.denominator for i in p_accum], 1)
        res     = map(lambda i: int(i.numerator * lcm_res / i.denominator), p_accum) + [int(lcm_res)]

        return res

    # define helper functions here
    def lcm(a, b):
        return a * b // gcd(a, b)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def identityMatrix(size):
        I = [[0 for i in range(size)] for j in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                if i == j: I[i][j] = 1
        return I

    #adapted from http://codegist.net/snippet/python/multip_matrixpy_volf52_python
    def multiplyMatrices(X, Y):
        return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]

    def subtractMatrices(X, Y):
        res = [[0 for i in range(len(X))] for j in range(len(X))]
        for i in range(0, len(X)):
            for j in range(0, len(Y)):
                res[i][j] = X[i][j] - Y[i][j]
        return res

    def identifyZeros(X, i, j):
        nz = []
        fnz = -1
        for m in range(i, len(X)):
            nz_bool = X[m][j] != 0
            nz.append(nz_bool)
            if fnz == -1 and nz_bool:
                fnz = m
        z_sum = sum(nz)
        return z_sum, fnz

    def swap_row(X, i, p):
        X[p], X[i] = X[i], X[p]
        return X

    #adapted from http://www.vikparuchuri.com/blog/inverting-your-very-own-matrix/
    def invertMatrix(X):

        rows = len(X)
        I = identityMatrix(rows)

        for i in range(0, rows):
            X[i] += I[i]

        i = 0
        for j in range(0, rows):
            z_sum, fnz = identifyZeros(X, i, j)
            if z_sum == 0:
                if j == rows:
                    #matrix is singular
                    return None
            if fnz != i:
                X = swap_row(X, i, fnz)
            X[i] = [m / X[i][j] for m in X[i]]
            for q in range(0, rows):
                if q != i:
                    scaled_row = [X[q][j] * m for m in X[i]]
                    X[q] = [X[q][m] - scaled_row[m] for m in range(0, len(scaled_row))]
            if i == rows or j == rows:
                break
            i += 1
        for i in range(0, rows):
            X[i] = X[i][rows:len(X[i])]

        return X


    return main(m)

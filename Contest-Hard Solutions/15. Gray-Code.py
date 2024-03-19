def getGray(n):
    return n^(n>>1)

def grayCode(n):
    n = 1<<n
    res = [0]*n
    for i in range(n):
        res[i] = getGray(i)
    return res
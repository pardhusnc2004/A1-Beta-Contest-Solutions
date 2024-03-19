def xorQueries(arr, queries):
    d = [0]+arr
    for i in range(1, len(d)):
        d[i] ^= d[i-1]
    return [d[r+1]^d[l] for l, r in queries]
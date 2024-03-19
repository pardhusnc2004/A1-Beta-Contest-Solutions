def hasAlternatingBits(n):
    fl = n&1
    while n:
        # print(n, fl)
        if fl:
            fl = 0
            if not n&1:
                return False
        else:
            fl = 1
            if n&1:
                return False
        n>>=1
    return True
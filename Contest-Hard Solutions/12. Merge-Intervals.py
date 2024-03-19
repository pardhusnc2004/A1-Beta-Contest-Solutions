def merge(intervals):
    intervals = sorted(intervals, key = lambda x:[x[0]])
    res = []
    for i in intervals:
        if not res:
            res.append(i)
        else:
            if res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
    return res
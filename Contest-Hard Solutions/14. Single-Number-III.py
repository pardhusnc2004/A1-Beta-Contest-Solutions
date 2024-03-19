from collections import Counter

def singleNumber(nums):
    c = Counter(nums)
    res = []
    for i in c:
        if c[i] == 1:
            res.append(i)
            if len(res)==2:
                break
    return res
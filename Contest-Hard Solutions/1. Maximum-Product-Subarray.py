def maxProduct(nums):
    res = -1e9
    pref, suff = 1, 1
    
    for i in nums:
        pref *= i
        res = max(res, pref)
        if not pref:
            pref = 1
    
    for i in reversed(nums):
        suff *= i
        res = max(res, suff)
        if not suff:
            suff = 1
    
    return res
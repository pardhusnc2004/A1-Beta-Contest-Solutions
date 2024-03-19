def singleNumber_O_n_space(nums):
    hm = {}
    for i in nums:
        hm[i] = hm.get(i, 0)+1
    for i in hm:
        if hm[i] == 1:
            return i
    return -1

def singleNumber_O_1_space(nums):
    ones, twos = 0, 0
    for i in nums:
        ones ^= (i&~twos)
        twos ^= (i&~ones)
    return ones
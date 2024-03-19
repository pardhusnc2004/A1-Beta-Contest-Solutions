def sub_array_0_sum_exists(arr,n):
    d = {}
    cursum = 0
    for i in arr:
        cursum += i
        if not cursum:
            return True
        if cursum in d:
            return True
        d[cursum] = 1
    return False
def checkSubarraySum(nums, k):
    for i, n in enumerate(nums):
        nums[i] = n%k
    cursum = 0
    d = {0:-1}
    for i in range(len(nums)):
        cursum += nums[i]
        req = cursum%k
        if req in d:
            if i-d[req] >= 2:
                return True
        else:
            d[cursum%k] = i
    return False
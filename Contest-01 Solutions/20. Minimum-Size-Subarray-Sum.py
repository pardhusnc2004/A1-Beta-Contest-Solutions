def minSubArrayLen(target, nums):
    cursum = 0
    left = 0
    res = len(nums)+1
    for i in range(len(nums)):
        cursum += nums[i]
        while cursum >= target:
            cursum -= nums[left]
            res = min(res, i-left+1)
            left += 1
    if res == len(nums)+1:
        return 0
    return res
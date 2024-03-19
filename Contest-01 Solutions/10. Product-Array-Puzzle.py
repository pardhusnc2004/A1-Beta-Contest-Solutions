def productExceptSelf(nums):
    
    pref = nums[0]
    res = [1]*len(nums)
    for i in range(1,len(nums)):
        res[i] = pref
        pref *= nums[i]
        
    suff = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        res[i]*=suff
        suff*=nums[i]
    return res
def waysToMakeFair(nums):
    even, odd = 0, 0
    for i in range(1, len(nums)):
        if i&1:
            even+=nums[i]
        else:
            odd+=nums[i]
    ctr = 0
    
    if even==odd:
        ctr+=1
        
    for i in range(1, len(nums)):
        if i&1:
            even+=nums[i-1]-nums[i]
        else:
            odd+=nums[i-1]-nums[i]
        if even == odd:
            ctr+=1
    return ctr
def reverse(nums, l, r):
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1

def nextPermutation(nums):
    n = len(nums)
    if n==1:
        return
    r = n-2
    
    while r>=0 and nums[r]>=nums[r+1]:
        r-=1
        
    if r>=0:
        j = n-1
        while nums[j]<=nums[r]:
            j-=1
        nums[j], nums[r] = nums[r], nums[j]
    reverse(nums, r+1, n-1)
    return nums
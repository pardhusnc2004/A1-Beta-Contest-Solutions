def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

# Cyclic Sort Approach
def firstMissingPositive(nums):
    i = 0
    n = len(nums)
    while i<n:
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]:
            swap(nums, i, nums[i]-1)
        else:
            i+=1
    for i in range(n):
        if nums[i] != i+1:
            return i+1
    
    return n+1

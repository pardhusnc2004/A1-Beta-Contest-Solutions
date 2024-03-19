def maxResult(nums, k):
    # Time Limit Exceeded
    # Contraints: K => 10^5
    #             N => 10^5
    
    n = len(nums)
    dp = [0]*(n)
    dp[-1] = nums[-1]
    for i in range(n-2, -1, -1):
        maxScore = -1e9
        for jump in range(1,k+1):
            # print(i, nums[i], dp[min(n-1, i+jump)])
            maxScore = max(maxScore, nums[i]+dp[min(n-1, i+jump)])
        dp[i] = maxScore
    # print(dp)
    return dp[0]
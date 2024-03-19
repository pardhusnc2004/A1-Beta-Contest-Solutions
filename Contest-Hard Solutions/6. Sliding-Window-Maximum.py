from collections import deque

def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    dq = deque()
    res = []
    for i in range(len(nums)):
        if dq and dq[0] == i-k:
            dq.popleft()
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k-1:
            res.append(nums[dq[0]])
    return res
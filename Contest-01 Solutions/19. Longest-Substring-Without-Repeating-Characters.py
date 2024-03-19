def lengthOfLongestSubstring(s):
    d = {}
    left = 0
    res = 0
    for i in range(len(s)):
        d[s[i]] = [d.get(s[i], [0,-1])[0]+1, i]
        if d[s[i]][0] > 1:
            while d[s[i]][0] > 1 and left < i:
                d[s[left]][0] -= 1
                left += 1
        res = max(res, i-left+1)
    return res
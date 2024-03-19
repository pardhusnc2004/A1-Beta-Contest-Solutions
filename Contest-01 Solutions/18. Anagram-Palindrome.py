from collections import Counter

def isPossible(S):
    c = Counter(S)
    odds = 0

    for i in c:
        if c[i]%2:
            odds+=1
            if odds > 1:
                return False
    return True
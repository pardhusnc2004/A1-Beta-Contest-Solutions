def groupAnagrams(strs):
    d = {}
    for i in strs:
        ex = ''.join(sorted(list(i)))
        if ex in d:
            d[ex].append(i)
        else:
            d[ex] = [i]
    return sorted(d.values())
def trap(a):
    n = len(a)
    lmax, rmax = 0, 0
    l, r = 0, n-1
    res = 0
    
    while l<=r:
        if a[l] <= a[r]:
            if a[l] > lmax:
                lmax = a[l]
            else:
                res += lmax-a[l]
            l+=1
        else:
            if a[r] > rmax:
                rmax = a[r]
            else:
                res += rmax-a[r]
            r-=1
    return res
def isPowerOfFour(n):
    if n <= 0:
        return False
    return (n&(n-1)) == 0 and not (n-1)%3
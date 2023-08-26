def my_func():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    ind = 0
    res = 0
    maxi = 0
    start = 0
    while ind < n:
        
        t -= a[ind]
        res += 1
        while t < 0:
            t += a[start]
            start += 1
            res -= 1
        maxi = max(maxi, res)
        ind += 1
    print(res)
my_func()
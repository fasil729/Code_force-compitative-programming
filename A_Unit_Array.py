import math


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ind = 0
    count = 0
    while ind < n and arr[ind] == -1:
        count += 1
        ind += 1
    res = 0
    tot = (-1 * count) + (n - ind)
    
    if tot < 0:
        res = math.ceil((-1 * tot) / 2)
        count -= res
    if count % 2 != 0:
        res += 1
    print(res)
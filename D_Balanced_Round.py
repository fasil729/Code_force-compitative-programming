t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split())) 
    res = 1
    count = 0
    arr.sort()
    ind = 0
    while ind < n - 1:
        if abs(arr[ind] - arr[ind + 1]) <= k:
            count += 1
        else:
            count = 0
        res = max(res, count + 1)
        ind += 1
    print(n - res)

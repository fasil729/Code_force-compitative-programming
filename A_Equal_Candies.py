t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mini = min(arr)
    res = 0
    for a in arr:
        res += a - mini 
    print(res)
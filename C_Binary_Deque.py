t = int(input())

for _ in range(t):
    n, s = map(int, input().split())

    a = list(map(int, input().split()))

    tot = s
    temp = 0
    start = 0
    ans = -1

    for end in range(n):
        temp += a[end]
        while start <= end and temp > tot:
            temp -= a[start]
            start += 1
        
        if temp == tot:
            ans = max(ans, end - start + 1)
    
    if ans == -1:
        print(-1)
    else:
        
        print(n - ans)
        
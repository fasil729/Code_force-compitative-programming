q = int(input())

for _ in range(q):
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mini = t
    ans = -1
    res = 0
    for ind, num in enumerate(a):
        if mini >= num and ans < b[ind]:
            ans = b[ind]
            res = ind + 1
        mini -= 1
      
    if ans != -1:
        print(res)
    else:
        print(-1)


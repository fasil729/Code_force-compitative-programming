import math

def myfunc():
    
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    vis = set()
    for num in a:
        if not num in vis:
            res += 1
            vis.add(num)
    ans = []
    for i in range(n):
        if (i + 1) > res:
            ans.append(str(i + 1))
        else:
            ans.append(str(res))
    print(" ".join(ans))

t = int(input())
for _ in range(t):
    myfunc()
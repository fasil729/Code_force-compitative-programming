import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        d, s = map(int, input().split())
        arr.append((d, (s - 1) // 2 + d))
    mini = float("inf")
    arr.sort()
    for ind in range(n):
        mini = min(mini, arr[ind][1])
        if mini <= arr[ind][0]:
            break
    print(mini)
        

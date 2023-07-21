from collections import defaultdict
import heapq

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    used = set()
    maxi = defaultdict(lambda: [0, 0])
    last = defaultdict(lambda: -1)
    for ind, p in enumerate(arr):
        diff = ind - last[p] - 1
        last[p] = ind
        heapq.heappushpop(maxi[p], diff)
        
    res = float("inf")
 
    for key, value in maxi.items():
        heapq.heappushpop(value, n - last[key] - 1)
        second, first = value
        res = min(res, max(first // 2, second))
    print(res)
    



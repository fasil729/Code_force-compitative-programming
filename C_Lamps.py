from collections import defaultdict
import heapq


t = int(input())

for _ in range(t):
    n = int(input())
    dic = defaultdict(list)
    for i in range(n):
        a, b = map(int, input().split())
        heapq.heappush(dic[a], -1 * b)
    
    res = 0
    for key, value in dic.items():
        c = 0
        while value and c < key:
            res += -1 * heapq.heappop(value)
            c += 1
    print(res)
    

    
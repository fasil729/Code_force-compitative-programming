from heapq import heapify, heappop

def myfunc():
    
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pair = [(a[i], b[i]) for i in range(n)]
    heapify(pair)
    res = k
    while pair and res >= pair[0][0]:
        res += heappop(pair)[1]
    print(res)

t = int(input())
for _ in range(t):
    myfunc()
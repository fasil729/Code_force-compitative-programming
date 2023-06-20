import heapq


t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    heapq.heapify(a) 
    b = list(map(lambda x: int(x), input().split()))
    heapq.heapify(b)
     
    while b:
        b_l = heapq.heappop(b)
        heapq.heappop(a)
        heapq.heappush(a, b_l)
        
    print(sum(a))



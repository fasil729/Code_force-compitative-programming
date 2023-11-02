from collections import defaultdict
import heapq

n, m = map(int, input().split())
graph = defaultdict(set)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].add((v, w))
    graph[v].add((u, w))

def dijkstra(start):
    heap = [(0, start)]
    ans = {key:(float("inf"), -1) for key in range(1, n + 1)}
    ans[1] = (0, -1)
    while heap:
        dist, node = heapq.heappop(heap)
        if node == n:
            return ans
        
        for neigh, cost in graph[node]:
            new_dist = dist + cost
            if ans[neigh][0] > new_dist:
                ans[neigh] = (new_dist, node)
                heapq.heappush(heap, (new_dist, neigh))
            
            
    return -1
dist = dijkstra(1)
if dist == -1:
    print(-1)
else:
    ans = [str(n)]
    prev = n
    while dist[prev][1] != 1:
    
        ans.append(str(dist[prev][1]))
        prev = dist[prev][1]
    ans.append("1")
    print(" ".join(ans[::-1]))

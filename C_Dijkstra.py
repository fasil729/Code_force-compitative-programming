from collections import defaultdict
import heapq

n, m = map(int, input().split())
graph = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
    
def train(start):
    heap = [(0, start)]
    visited = set()
    while heap:
        dist, node = heapq.heappop(heap)
        if node == n:
            return dist
        visited.add(node)
        
        for neigh in graph[node]:
            if neigh in visited:
                continue
            new_dist = dist + 1
            heapq.heappush(heap, (new_dist, neigh))
    return -1
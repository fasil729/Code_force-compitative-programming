from collections import defaultdict
import heapq

n, m = map(int, input().split())
graph = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)


def bus(start):
    heap = [(0, start)]
    visited = set([start])
    while heap:
        dist, node = heapq.heappop(heap)
        if node == n:
            return dist
        
        
        for neigh in range(1, n + 1):
            if neigh in graph[node] or neigh in visited:
                continue
            visited.add(neigh)
            new_dist = dist + 1
            heapq.heappush(heap, (new_dist, neigh))
    return -1

def train(start):
    heap = [(0, start)]
    visited = set([start])
    while heap:
        dist, node = heapq.heappop(heap)
        if node == n:
            return dist
        
        
        for neigh in graph[node]:
            if neigh in visited:
                continue
            visited.add(neigh)
            new_dist = dist + 1
            heapq.heappush(heap, (new_dist, neigh))
    return -1

t = train(1)
b = bus(1)
if b == -1 or t == -1:
    print(-1)
else:
    print(max(t, b))


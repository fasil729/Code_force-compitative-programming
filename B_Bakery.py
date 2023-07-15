from collections import defaultdict
import heapq

def main():
    n, m , k = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        v, u, cost = map(int, input().split())
        heapq.heappush(graph[u], (cost,  v))
        heapq.heappush(graph[v], (cost, u))

    if k == 0:
        print(-1)
        return
    
    flour = list(map(int, input().split()))

    visited = set(flour)
    mini = float("inf")
    for f in flour:
        if not graph[f]:
            continue
        dist, node = heapq.heappop(graph[f])
        while node in visited and graph[f]:
            dist, node = heapq.heappop(graph[f])
        if node not in visited:
            mini = min(mini, dist)
    if mini != float("inf"):
        print(mini) 
    else: 
        print(-1)
    return 
main()


   

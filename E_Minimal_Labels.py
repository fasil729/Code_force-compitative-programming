from collections import defaultdict
import heapq


n, m = map(int, input().split())
graph = defaultdict(list)
indegree = {i:0 for i in range(1, n + 1)}
ans = [0] * n
for _ in range(m):
    v, u = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1
queue = [-i for i in indegree if indegree[i] == 0]
heapq.heapify(queue)
label = n

while queue:
    node = heapq.heappop(queue)
   
    
    node = -1 * node
    ans[node - 1] = str(label)
    label -= 1
    for neigh in graph[node]:
        indegree[neigh] -= 1
        if indegree[neigh] == 0:
            heapq.heappush(queue, -neigh)
   
print(" ".join(ans))


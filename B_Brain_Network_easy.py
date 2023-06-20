from collections import defaultdict, deque


n, m = map(int, input().split())
graph = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs():
    que = deque([a])
    visited = set()
    while que:
        num = que.popleft()
        if num in visited:
            return False
            
        
        visited.add(num)
        for neigh in graph[num]:
            que.append(neigh)
            graph[neigh].remove(num)
    if len(visited) == n:
        return True
    return False

if bfs():
    print("yes")
else:
    print("no")


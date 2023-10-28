from collections import defaultdict, deque
t = int(input())

def bfs(graph, x):
    queue = x + [1]
    color = {k: 1 for k in x}
    color[1] = 0
    while queue:
        new_queue = []
        for q in queue:
             c = color[q]
             for neigh in graph[q]:
                 if neigh not in color:
                     new_queue.append(neigh)
                     color[neigh] = c
        queue = new_queue
    for node in graph:
        if node != 1 and len(graph[node]) == 1 and color[node] == 0:
            print("YES")
            return
    print("NO")
    return

for _ in range(t):
    input()
    graph = defaultdict(list)
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    for i in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    bfs(graph, x)




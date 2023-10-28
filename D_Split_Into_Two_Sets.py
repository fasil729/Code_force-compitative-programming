from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[u].append(v)
    color = defaultdict(int)

    def check_bipartite(node, c):
        if node in color and color[node] == c:
            return False
        if node in color:
            return True
        
        color[node] = 1 - c
        ans = True
        for neigh in graph[node]:
            ans = ans or check_bipartite(neigh, 1 - c)
        return ans
    
    ans = True
    for node in graph:
        if node in color:
            continue
        ans = ans or check_bipartite(node, 0)
    if ans:
        print("YES")
    else:
        print("NO")

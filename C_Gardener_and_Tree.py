from collections import defaultdict


t = int(input())

for _ in range(t):
    input()
    n, k = map(int, input().split())
    graph = defaultdict(set)
    for i in range(n - 1):
        v, u = map(int, input().split())
        graph[v].add(u)
        graph[u].add(v)
    print(graph)
    k = 1 
    while k:
        items = [(key, adj.copy()) for key, adj in graph.items()]
        
        for key, adj in items:
            if len(adj) == 0:
                print(items)
                print(key, "0")
                del graph[key]
                continue
            if len(adj) == 1:
                # print(items, items)
                print(key, adj, "1")
                adj = [neigh for neigh in adj]
                if adj[0] in graph:
                    graph[adj[0]].remove(key)
                del graph[key]
        k -= 1
    print(graph)
    ans = 0
    for key in graph:
        
        ans += 1
    print(ans)



        


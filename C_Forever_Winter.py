from collections import defaultdict
t = int(input())

def func():
    for n in graph:
        if len(graph[n]) == 1:
            leaf_node = n
            break
  
    middle_node = graph[leaf_node][0]
    for neigh in graph[middle_node]:
        if len(graph[neigh]) != 1:
            center = neigh
            break
    
    y = len(graph[middle_node]) - 1
    x = len(graph[center])

    return x, y


for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    x, y = func()
    print(x, y)


    



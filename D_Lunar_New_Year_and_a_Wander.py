from collections import defaultdict


def dfs(node, move):
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


n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)
x, y = dfs("1", 0)
print(x, y)


    



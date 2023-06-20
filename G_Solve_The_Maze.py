from collections import  deque

t = int(input())


n, m = map(int, input().split())
graph = []
goods = 0

for _ in range(m):
    s = input()
    graph.append(a)
    for a in s:
        if a == "G":
            goods += 1
   

def bfs(row, col):
    que = deque((row, col, 0))
    visited = set()
    while que:
        row, col, num = que.popleft()
        if (row, col) in visited:
            return num == goods
            
        
        visited.add((row, col))
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
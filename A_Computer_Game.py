from collections import deque
t = int(input())

def bfs(level):
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
    que = deque([(0, 0)])
    visited = set()
    while que:
        row, col = que.popleft()
        if (row, col) in visited:
            continue
        if (row, col) == (1, n - 1):
            return True
            
        
        visited.add((row, col))
       
        for r, c in direction:
            nr = row + r
            nc = col + c
            
            if 0 <= nr < 2 and 0 <= nc < n and level[nr][nc] == "0":
                que.append((nr, nc))
    return False

for _ in range(t):
    n = int(input())
    level = []
    level.append(input())
    level.append(input())
    if bfs(level):
        print("YES")
    else:
        print("NO")
    

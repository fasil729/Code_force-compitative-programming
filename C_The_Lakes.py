from collections import deque
t = int(input())


def bfs(row, col):
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    que = deque([(row, col)])
    vol = 0
    while que:
        row, col = que.popleft()
        if (row, col) in visited:
            continue
        
            
        vol += maze[row][col]
        visited.add((row, col))
       
        for r, c in direction:
            nr = row + r
            nc = col + c
            
            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc]:
                que.append((nr, nc))
    return vol

for _ in range(t):
    n, m = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input().split())))
    visited = set()
    res = 0

    for r in range(n):
        for c in range(m):
            if (r, c) not in visited and maze[r][c]:
                res = max(res, bfs(r, c))

    print(res)

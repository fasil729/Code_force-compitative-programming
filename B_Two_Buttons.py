from collections import deque
n, m = map(int, input().split())

def bfs():
    que = deque([(n, 0)])
    visited = set()
    while que:
        num, count = que.popleft()
        if num in visited:
            continue
        if num == m:
            return count
            
        
        visited.add(num)
        if num <= m:
            que.append((num * 2, count + 1))
        if num - 1 > 0 and num - 1 >= num // 2:
            que.append((num - 1, count + 1))
                
print(bfs())
    

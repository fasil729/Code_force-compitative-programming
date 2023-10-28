n = int(input())
graph = {}
p = list(map(int, input().split()))



def dp(node):
    if node in visited:
        return str(node)
    visited.add(node)
    
    return dp(p[node - 1])

ans = []
for i in range(n):
    visited = set()
    ans.append(dp(i + 1))
print(" ".join(ans))
    

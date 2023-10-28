class UnionFind:
    def __init__(self, n, m):
        self.root = {(i, j):(i, j) for i in range(n) for j in range(m)}
        self.rank = {(i, j):1 for i in range(n) for j in range(m)}

    def find(self, x):
        if self.root[x] == x:
            return self.root[x]
        # self.root[x] = self.find(self.root[x])
        return self.find(self.root[x])
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return

        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx 
            self.rank[rootx] += self.rank[rooty]
        else:
            self.root[rootx] = rooty 
            self.rank[rooty] += self.rank[rootx]

    def get_rank(self, x):
        return self.rank[self.find(x)]

    
def num_compenent(i, j, uf):
    direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    check = set()

    res = 1
    for r, c in direc:
        nc = j + c
        nr = i + r
        braked = False
        if 0 <= nr < n and 0 <= nc < m and g[nr][nc] == ".":
            for x in check:
                if uf.find(x) == uf.find((nr, nc)):
                    braked = True
                    break
            check.add((nr, nc))   
            if braked:
                continue
            res += uf.get_rank((nr, nc))
        
    return res


                    



n, m = map(int, input().split())
g = []
ans = ["" for i in range(n)]
for i in range(n):
    arr = []
    for char in input():
        arr.append(char)
    g.append(arr)

direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

uf = UnionFind(n, m)
for i in range(n):
    for j in range(m):
        if g[i][j] == "*":
            continue
        for r, c in direc:
            nc = j + c
            nr = i + r
            if 0 <= nr < n and 0 <= nc < m and g[nr][nc] == ".":
                    uf.union((i, j), (nr, nc))
for i in range(n):
    for j in range(m):
        if g[i][j] == ".":
            ans[i] += "."
        else:
            ans[i] += str(num_compenent(i, j, uf) % 10)

for a in ans:
    print(a)
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x]) # path compression
        return self.root[x]
       
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:   # optimizing union functtion using rank
                self.root[rootY] = rootX
                
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1



def solution():
    n, m, d = map(int, input().split())

    uf_m = UnionFind(n)
    uf_d = UnionFind(n)

    for _ in range(m):
        v, u = map(int, input().split())
        uf_m.union(v - 1, u - 1)
    for _ in range(d):
        v, u = map(int, input().split())
        uf_d.union(v - 1, u - 1)
    res = []
    for i in range(n):
        for j in range(n):
            if uf_d.find(i) != uf_d.find(j) and uf_m.find(i) != uf_m.find(j):
                uf_m.union(i, j)
                uf_d.union(i, j)
                res.append((i + 1, j + 1))

    print(len(res))
    for u, v in res:
        print(u, v)
    return
solution()
class UnionFind:
    def __init__(self, string):
        self.root = {char:char for char in string}
        self.rank = {char:0 for char in string}

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

def my_func():
    n = int(input())
    s_1= input()
    s_2 = input()
    uf = UnionFind(s_1 + s_2)
    ans = []   
    for i in range(len(s_1)):
        if uf.find(s_1[i]) != uf.find(s_2[i]):
            uf.union(s_1[i], s_2[i])
            ans.append((s_1[i], s_2[i]))
    print(len(ans))
    for c1, c2 in ans:
        print(c1, c2) 
my_func()          
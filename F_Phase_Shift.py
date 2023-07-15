import heapq
class UnionFind:
    def __init__(self, root, rank):
        self.root = root
        self.rank = rank

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
    t = int(input())
    root = {chr(order): chr(order) for order in range(97, 123)}
    rank = {chr(order): 0 for order in range(97, 123)}
    for _ in range(t):
        n = int(input())
        t = input()
        uf = UnionFind(root.copy(), rank.copy())
        letters = {}
        heap = [chr(order) for order in range(97, 123)]
        heapq.heapify(heap)
        s = ""
        for char in t:
            if char in letters:
                s += letters[char]
            else:
                let = heapq.heappop(heap)
                if heap:
                    if uf.find(let) == uf.find(char):
                        let = heapq.heapreplace(heap, let)
                uf.union(let, char)
                s += let
                letters[char] = let
        print(s)
    
solution()
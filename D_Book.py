from collections import defaultdict

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        colors = [0 for _ in range(n)]
        order = []

        

        for node in range(n):
            if colors[node] != 0:
                continue
            self.topSort(node, colors, graph, order)
                
                

        return len(order)
    def topSort(self, node, colors, graph, order):
        # Cycle found - Why?
        if colors[node] == 1:
            return False

        colors[node] = 1
        for neighbor in graph[node]:
            if colors[neighbor] == 2:
                continue
            if not self.topSort(neighbor, colors, graph, order):
                return False

        # Color nodes black as we backtrack
        colors[node] = 2
        order.append(node)
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        req = list(map(int, input().split()))
        for j in req:
            graph[j].append(i)
    sol = Solution()
    print(sol.eventualSafeNodes(graph))



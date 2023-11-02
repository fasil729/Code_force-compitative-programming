from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    graph = defaultdict(set)
    for i in range(n):
        graph[i].add(arr[i] - 1)
        graph[arr[i] - 1].add(i)
    
    visited = set()
    bamboos, cycles = 0, 0
    for i in range(n):
        if i not in visited:
            stack = [i]
            compenent = []
            
            while stack:
                node = stack.pop()
                visited.add(node)
                compenent.append(node)
                for neigh in graph[node]:
                    if neigh not in visited:
                        stack.append(neigh)
                        
                        

            bamboo = False
            # print(graph)
            for node in compenent:
                if len(graph[node]) == 1:
                    bamboo = True
                    break
            
            if bamboo:
                bamboos += 1
            else:
                cycles += 1
    # print(cycles, bamboos, "cycles")
    print(cycles + min(bamboos, 1), cycles + bamboos)


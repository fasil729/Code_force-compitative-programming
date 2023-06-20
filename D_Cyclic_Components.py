from collections import defaultdict

def main():
    n, m = map(int, input().split())
   
    graph = defaultdict(list)

    for _ in range(m):
        i, j = map(int, input().split())
        graph[i - 1].append(j - 1)
        graph[j - 1].append(i - 1)
   

    visited= set()
    def dfs(node):

        stack = [node]
        
        
        
        cycle = True
        while stack:
            curr = stack.pop()
            if len(graph[curr]) != 2:
                cycle = False
            visited.add(curr)
            for neigh in graph[curr]:
                if not neigh in visited:
                    stack.append(neigh)
        return cycle
    # print(graph)
    # print("here", dfs(0))
    
    res = 0
    for node in range(n):
        # print(node)
        if not node in visited and dfs(node):
            res += 1
    print(res)

if __name__ == '__main__':
    main()
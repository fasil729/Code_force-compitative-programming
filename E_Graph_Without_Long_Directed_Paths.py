from collections import defaultdict

def main():
    n, m = map(int, input().split())
    arr = []
    graph = defaultdict(list)

    for _ in range(m):
        i, j = map(int, input().split())
        graph[i - 1].append(j - 1)
        graph[j - 1].append(i - 1)
        arr.append(i - 1)
   
  
    visited= set()
    direc = [0] * n
    def dfs(node, status):
        stack = [(node, status)]
        while stack:
            node, status = stack.pop()
            
            
            direc[node] = status    
            visited.add(node)
            for neigh in graph[node]:
                if neigh in visited and direc[neigh] == status:
                    return False
                if not neigh in visited:
                    stack.append((neigh, 1 - status))
            
        return True
       
    # print("here", dfs(0))
    
    if dfs(0, 1):
        print("YES")
        res = ""
        for i in arr:
            res += str(direc[i])
        print(res)
    else:
        print("NO")

if __name__ == '__main__':
    
    main()


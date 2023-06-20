from collections import defaultdict
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    graph = defaultdict(list)

    for _ in range(m):
        i, j = map(int, input().split())
        graph[i - 1].append(j - 1)
        graph[j - 1].append(i - 1)
   

    visited= set()
    def dfs(node):
        if node in visited:
            return float("inf")
        visited.add(node)
        mini = c[node]
        for neigh in graph[node]:
            mini = min(dfs(neigh), mini)
        return mini
    # print("here", dfs(0))
    
    res = 0
    for node in range(n):
        if not node in visited:
            res += dfs(node)
    print(res)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

import sys, threading

input = lambda: sys.stdin.readline().strip()
def main():
    n = int(input())
    r_s, c_s = map(int, input().split())
    r_g, c_g = map(int, input().split())

    mat = []
    for _ in range(n):
        mat.append(input())

    def calc(s, g):
        return (s[0] - g[0]) ** 2 + (s[1] - g[1]) ** 2

    def dfs(row, col, visited):
        if (row, col) in visited or not (0 <= row < n and 0 <= col < n) or mat[row][col] == "1" :
            return
        direc = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        visited.add((row, col))

        for r, c in direc:
            dfs(row + r, col + c, visited)

    visited = set()
    dfs(r_s - 1, c_s - 1, visited)
    if (r_g - 1, c_g - 1) in visited:
        print(0)
        return
    start = list(visited)
    visited = set()
    dfs(r_g - 1, c_g - 1, visited)
    end = list(visited)
    res = float("inf")
    for s in start:
        for e in end:
            res = min(res, calc(s, e))
    print(res)




if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
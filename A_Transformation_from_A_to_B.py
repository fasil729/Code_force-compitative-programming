import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    a, b = map(int, input().split())
    path = [str(a)]
    def dfs(a, b):
        
        if a > b:
            return False, path
        if a == b:
            return True, path
        path.append(str(a * 2))
        if dfs(a * 2, b)[0]:
            return True, path
        path.pop()
        path.append(str((a * 10) + 1) )
        if dfs((a * 10) + 1, b)[0]:
            return True, path
        path.pop()
        return False, path
    is_exist, new_path = dfs(a, b)
    if is_exist:
        print("YES")
        print(len(new_path))
        print(" ".join(new_path))
    else:
        print("NO")

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()



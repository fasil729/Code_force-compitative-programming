import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = input()
    def dfs(num):
        if num == n:
            return True
        if len(num) > len(n):
            return False
        return dfs(num + "1") or dfs(num + "14") or dfs(num + "144")
    if dfs(""):
        print("YES")
    else:
        print("NO")
        
      

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()



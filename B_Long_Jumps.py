import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        n = len(arr)
        memo = {}
        def dp(ind):
            if ind in memo:
                return memo[ind]
            if ind >= n:
                return 0
            a = arr[ind]
            memo[ind] = a + dp(ind + a)
            return memo[ind]
        
        ans = 0
        for i in range(n):
            ans = max(ans, dp(i))
        
        print(ans)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




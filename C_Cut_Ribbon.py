

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, a, b, c = map(int, input().split())

  
    memo = {}
    def dp(leng):
        if leng in memo:
            return memo[leng]
        if leng == 0:
            return 0
        ans = float("-inf")
        if leng - a >= 0:
            ans = max(ans, dp(leng - a) + 1)
        if leng - b >= 0:
            ans = max(ans, dp(leng - b) + 1)
        if leng - c >= 0:
            ans = max(ans, dp(leng - c) + 1)
        
        memo[leng] = ans
        return ans
        
    print(dp(n))

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




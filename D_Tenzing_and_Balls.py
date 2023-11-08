import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        nums = {}
        next = [i for i in range(n)]
        for i in range(n - 1, -1, -1):
            num = arr[i]
            if num in nums:
                next[i] = nums[num]
            if not num in nums:
                nums[num] = i
        n = len(arr)
        print(next)
        memo = {}
        def dp(ind):
            if ind in memo:
                return memo[ind]
            if ind >= n:
                return 0
            ans = 0
            j = next[ind]
            if j != ind:
                ans = min(ans, dp(j + 1))
            ans = min(ans, dp(ind + 1) + 1)
            
            memo[ind] = ans
            return memo[ind]
        
    
        print(n - dp(0))

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




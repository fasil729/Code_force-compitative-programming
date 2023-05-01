import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    # write your code here
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        res = [0] * n
        def recurse(start, end, depth):
            if start >= end:
                return
            maxi = 0
            for i in range(start, end):
                if arr[i] > maxi:
                    maxi = arr[i]
                    ind = i
            res[ind] = depth
            recurse(start, ind, depth + 1)
            recurse(ind + 1, end, depth + 1)
        recurse(0, n, 0)
        for num in res:
            print(num, end=" ")
        print()
        
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 15)
    threading.stack_size(1 << 15)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()



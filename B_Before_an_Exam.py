d, s = map(int, input().split())
arr = []
for _ in range(d):
    mini, maxi = map(int, input().split())
    arr.append([mini, maxi])
ans = []
 
def dp(index, s):
    if index == d:
        if s == 0:
            return True, ans
        return False, []
    mini, maxi = arr[index]
    for i in (mini, maxi):
        ans.append(str(i))
        res = dp(index + 1, s - i)
        if res[0]:
            return res
        ans.pop()
    return False, []

if dp(0, s)[0]:
    print("YES")
    print(" ".join(ans))
else:
    print("NO")


import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    # write your code here

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
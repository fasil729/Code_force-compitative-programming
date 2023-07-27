import math

def myfunc():
    
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ind = (n - 1)// 2
    right, left = 0, a[0]
    i = 1
    while i <= ind:
        right += a[-i]
        left += a[i]
        if right > left:
            print("yes")
            return
        i += 1
    print("no")
    

t = int(input())
for _ in range(t):
    myfunc()
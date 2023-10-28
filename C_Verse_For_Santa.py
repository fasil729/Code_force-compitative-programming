t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    if sum(arr) <= s:
        print(0)
        continue
    res = 0
    tot = 0
    maxi = 0
    for a in arr:
        tot += a
        maxi = max(maxi, a)
        if tot > s and tot - maxi > s:
            break
        else:
            res = maxi
    print(arr.index(res) + 1)
            
        
        
